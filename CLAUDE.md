# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 运行项目

```bash
# 安装依赖
pip install -r requirements.txt

# 启动应用
python main.py
```

本项目为 PySide6 桌面应用，所有 TODO 标记的位置需要逐步实现。

## 架构概览

项目采用 **MVC + Repository + Service** 分层架构，所有模块通过依赖注入组装（见 `main.py` 中的初始化顺序）。

**数据流方向**（单向，不可逆）：

```
View → Controller → Service → Repository → DBManager (SQLite)
                ↕
           SignalBus (跨模块广播)
```

- **View** 不可直接访问 Repository，由 Controller/Service 中转
- **Service** 之间通过 `SignalBus` 通信，禁止直接互相引用
- **Model**（dataclass）是纯数据结构，使用 `slots=True`，不含业务逻辑

## 分层职责

| 层 | 目录 | 职责 |
|---|------|------|
| Model | `models/` | `@dataclass(slots=True)` 纯数据，枚举定义在 `enums.py` |
| Repository | `database/repositories/` | 继承 `BaseRepository[T]`，封装所有 SQL，返回 Model 对象 |
| Service | `services/` | 业务逻辑，通过构造函数接收 Repository 实例（DI） |
| Controller | `controllers/` | 连接 View 信号与 Service 调用，持有 undo/redo 栈 |
| View | `views/` | PySide6 组件，信号发射给 Controller 或通过 SignalBus 订阅 |

## 关键设计模式

- **SignalBus**（`utils/signal_bus.py`）是全局单例信号总线，所有跨模块事件（`schedule_updated`、`setting_changed`、`timer_state_changed` 等）通过它广播，避免 Service 间直接耦合
- **日历策略模式**：`views/calendar/base_calendar_view.py` 定义抽象基类，`MonthView`/`WeekView`/`DayView` 实现策略，通过 `view_change_requested` 信号切换
- **ICommand**（`controllers/schedule_controller.py`）预留 undo/redo 接口，每个日程操作封装为 Command 对象推入双栈
- **Singleton**：`DBManager`、`SignalBus`、`SettingsManager`、`NotificationService` 使用 `__new__` + `_instance` 模式
- **Repository**：`BaseRepository[T]` 泛型抽象基类定义标准 CRUD，具体仓储实现可替换存储后端

## 数据库（6 表）

- `schedules` — 日程主表，`repeat_type` 为模板字段，实际展示由 `ScheduleService` 调用 `expand_repeat_schedule()` 动态展开
- `schedule_exceptions` — 重复日程中跳过的日期，与 `schedule_id` 唯一约束
- `timer_records` — 分段计时记录（允许暂停/继续），`total_duration` 为 aggregate
- `categories` / `app_settings` / `db_version`

时间字段统一 ISO 8601 文本存储（SQLite 无原生 datetime）。

## 通知系统（混合模式）

`NotificationService` 启动时：
1. 遍历所有未完成日程，为每个 `notify_before` / `deadline_notify` 注册 `QTimer.singleShot`
2. 启动一个 5 分钟间隔的兜底轮询 `QTimer`，查询未来 10 分钟内的通知，补注册遗漏
3. 单个日程变更时调用 `refresh_schedule(id)` 取消旧 timer 并重新注册

## 实现顺序

P1 → models 层（enums、dataclasses）
P2 → database 层（DBManager、迁移、三个 Repository）
P3 → config + utils 层（constants、SettingsManager、SignalBus、date_utils、logger）
P4 → services 层（先 schedule_service + timer_service，后 notification、statistics、import_export）
P5 → views 日历部分（base_calendar_view → month/day → week）
P6 → controllers + views 其余部分（sidebar、main_window、schedule_dialog、floating_window、stats_page、settings_dialog）

## 扩展示例

添加新视图类型（如年视图）：新建 `views/calendar/year_view.py`，继承 `BaseCalendarView`，实现三个抽象方法，在 `CalendarHeader` 中添加入口按钮。

添加新通知渠道（如邮件）：在 `NotificationService._create_notification()` 中扩展，无需修改其他模块。
