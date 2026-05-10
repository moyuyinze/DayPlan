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

## 阶段开发计划（对应 B站教程 BV1c84y1N7iL）

教程共 75 集，按 PySide6 知识点由浅入深编排。以下将每个教程章节映射到本项目要实现的文件。

> 用法：学完教程某一章节后，打开对应文件，用刚学到的知识消灭 TODO。

### 阶段 0：启动骨架（P002~P006）

| 教程 | 学到 | 在本项目中实践 |
|------|------|---------------|
| P002 环境搭建 | pip install PySide6 | 运行 `main.py` 验证环境 |
| P003 基础框架 | QApplication + QMainWindow | 理解 `main.py` 启动流程 |
| P004 三种基础控件 | QLabel、QPushButton、QLineEdit | `views/title_bar.py` — 自定义标题栏 |
| P005-006 Qt Designer | 用 Designer 拖控件 | 可选：用 Designer 画 ScheduleDialog 布局草稿 |

**目标：** 主窗口可启动，自定义标题栏可见。

### 阶段 1：信号与槽（P007~P008）

| 教程 | 学到 | 在本项目中实践 |
|------|------|---------------|
| P007 信号与槽 | clicked.connect() | `views/sidebar.py` — 按钮点击切换 QStackedWidget 页面 |
| P008 练手-计算器 | 信号传参 | 侧边栏置顶按钮：clicked → 切换 WindowStaysOnTopHint |

**目标：** 侧边栏可点击切换页面。

### 阶段 2：常用控件（P009~P019）

本阶段集中实现 `views/schedule/schedule_dialog.py`（日程编辑弹窗）

| 教程控件 | 在 ScheduleDialog 中的应用 |
|----------|---------------------------|
| P009 QComboBox | 分类下拉选择 |
| P010 QCheckBox | "截止前一天通知"、"跨天日程" |
| P013 QRadioButton | 优先级单选（低/中/高/紧急） |
| P014 QTextEdit / QPlainTextEdit | 备注/描述输入框 |
| P016 QSlider | 可选：通知提前时间的滑条 |
| P017 布局 | QFormLayout + QHBoxLayout 组织弹窗 |
| P018-019 控件总结 | QDateTimeEdit 选时间、QSpinBox 重复间隔 |

**目标：** 可创建/编辑日程的完整表单弹窗。

### 阶段 3：对话框类（P020~P025）

| 教程 | 学到 | 在本项目中实践 |
|------|------|---------------|
| P020 QMessageBox | 信息/警告/错误弹窗 | `utils/widget_utils.py` — 封装 show_info/error/confirm |
| P021 QInputDialog | 简单输入弹窗 | 统计页快速搜索日程标题 |
| P022 QFileDialog | 打开/保存文件 | `services/import_export_service.py` — JSON 导入导出选文件 |
| P023 练手 | 图像+滑条联动 | 独立小练习 |
| P024 QFontDialog | 字体选择 | SettingsDialog 字体设置 |
| P025 QColorDialog | 颜色选择 | 创建分类时选颜色 |

**目标：** 各处对话框完整可用。

### 阶段 4：子窗口与自定义信号（P026~P030）

| 教程 | 学到 | 在本项目中实践 |
|------|------|---------------|
| P026 子窗口开闭 | QDialog 模态/非模态 | `views/settings/settings_dialog.py` 模态弹窗 |
| P027 主→子传参 | 构造函数传参 | 编辑日程时传入 Schedule 对象 |
| P028 子→主传信号 | 自定义 Signal | 弹窗确认后发射信号返回修改数据 |
| P029 启动界面 | SplashScreen | **新建** `views/splash_screen.py` |
| P030 设置窗口传参 | 多种传参方式 | SettingsDialog 通过 SignalBus 通知全局 |

**目标：** 主窗口与子窗口双向通信，有启动画面。

### 阶段 5：菜单栏与上下文菜单（P031~P034）

| 教程 | 学到 | 在本项目中实践 |
|------|------|---------------|
| P031-032 QMenuBar + QMenu + QAction | 菜单栏结构 | `main_window.py` — 文件/编辑/帮助菜单 |
| P033 窗体上下文菜单 | contextMenuEvent | 主窗口空白处右键：新建日程、刷新 |
| P034 控件上下文菜单 | setContextMenuPolicy | `schedule_list_widget.py` 右键：编辑/删除/完成 |

**目标：** 菜单栏 + 右键菜单完成。

### 阶段 6：资源与主题美化（P035~P044）

| 教程 | 学到 | 在本项目中实践 |
|------|------|---------------|
| P036 内置图标 | QStyle.standardIcon() | 给按钮添加系统图标 |
| P037-038 资源文件 | .qrc + 编译 | 创建 `resources/resources.qrc` 管理图标 |
| P039 一键美化 | 加载 QSS | `resources/styles/light.qss` + `dark.qss` 切换 |
| P040 隐藏标题栏 | FramelessWindowHint | `views/title_bar.py` 替代系统标题栏 |
| P041-044 PyDracula | 第三方主题模板 | 可选：用 PyDracula 美化主窗口外观 |

**目标：** 亮/暗主题切换，窗口无边框美化。

### 阶段 7：QListWidget（P045~P051）

| 教程 | 学到 | 在本项目中实践 |
|------|------|---------------|
| P045 增删 | addItem / takeItem | `schedule_list_widget.py` 日程列表动态增删 |
| P046 删改查 | 列表项操作 | 列表内联编辑、删除确认 |
| P047-048 属性信号 | itemClicked | 点击列表项 → 右侧显示 ScheduleDetailWidget |
| P049 排序 | sortItems | 按时间/优先级排序 |
| P050 上下文菜单 | 右键菜单 | `schedule_list_widget.py` 右键菜单 |
| P051 选中选择 | 单选/多选 | 批量操作日程 |

**目标：** 日视图左侧日程列表完整可用。

### 阶段 8：QTableWidget（P052~P060）

| 教程 | 学到 | 在本项目中实践 |
|------|------|---------------|
| P052 创建填充 | setItem | `views/statistics/stats_page.py` 统计表格 |
| P053 表头样式 | setHorizontalHeaderLabels | 自定义表头 |
| P054 单元格属性 | setBackground 等 | 完成状态着色（已完成=灰、超时=红） |
| P055 自动排序 | setSortingEnabled | 点击表头排序 |
| P056 常用信号 | cellClicked | 点击行 → 显示日程详情 |
| P057 搜索跳转 | findItems | 统计页搜索框高亮匹配行 |
| P058 合并单元格 | setSpan | 按日期合并同类统计行 |
| P059 上下文菜单 | 右键菜单 | 表格右键操作 |
| P060 分页加载 | 分页逻辑 | 可选：大量数据时分页展示 |

**目标：** 统计页用 QTableWidget 展示数据。

### 阶段 9：MVC 模型/视图（P061~P067）

| 教程 | 学到 | 在本项目中实践 |
|------|------|---------------|
| P061 QStandardItemModel | Model 创建 | 用 Model 重构日程列表数据绑定 |
| P062 MVC 介绍 | 理解架构 | 对照本项目 MVC 分层理解 |
| P063 QTableView 编辑 | 表格编辑 | `stats_page.py` 用 QTableView 替代 QTableWidget |
| P064 表头自适应 | resizeMode | 自动列宽 |
| P065 过滤排序合并 | proxy model | 按分类/日期过滤统计 |
| P066 QSqlQueryModel | 只读 SQL Model | `schedule_repo.py` 可选 SQLModel 封装 |
| P067 QSqlTableModel | 读写 SQL Model | `schedule_repo.py` 替换为 SQLModel 读写 |

**目标：** Model/View 架构下数据绑定更高效。

### 阶段 10：QTabWidget + QTimer + QThread（P068~P073）

| 教程 | 学到 | 在本项目中实践 |
|------|------|---------------|
| P068 QTabWidget | 选项卡 | SettingsDialog 用 Tab 分页：通知/外观/通用 |
| P069 QTimer | 定时器 | `services/timer_service.py` 每秒 tick 更新跑表 UI |
| P070 processEvents | 保持 UI 响应 | 导入大量 JSON 时不卡界面 |
| P071-072 QThread | 子线程 | `services/notification_service.py` 轮询放子线程 |
| P073 阻塞线程 | 理解阻塞 | 通知轮询不用主线程 sleep |

**目标：** 计时实时刷新，通知不卡界面。

### 阶段 11：收尾（P074）

| 教程 | 学到 | 在本项目中实践 |
|------|------|---------------|
| P074 结语 | 整体回顾 | 全局测试、修 bug、PyInstaller 打包 .exe |

**目标：** 可发行的桌面应用。

### 补充练习页面（教程未覆盖但适合练手）

| 新建文件 | 练习内容 |
|---------|---------|
| `views/welcome_page.py` | 欢迎页，今日日程摘要 + 快捷操作入口 |
| `views/category_manager.py` | 分类管理页，QListWidget + 增删改 |
| `views/log_viewer.py` | 日志查看页，QPlainTextEdit 只读 |
| `views/about_dialog.py` | 关于弹窗，QLabel + 超链接 |

### 教程章节 ↔ 项目文件 速查表

```
P002-P006 → main.py, views/title_bar.py
P007-P008 → views/sidebar.py
P009-P019 → views/schedule/schedule_dialog.py
P020-P025 → utils/widget_utils.py, views/schedule/, services/import_export_service.py
P026-P030 → views/splash_screen.py, views/settings/settings_dialog.py
P031-P034 → views/main_window.py, views/schedule/schedule_list_widget.py
P035-P044 → resources/styles/, views/title_bar.py
P045-P051 → views/schedule/schedule_list_widget.py, views/schedule/schedule_detail_widget.py
P052-P060 → views/statistics/stats_page.py
P061-P067 → views/statistics/stats_page.py, database/repositories/
P068     → views/settings/settings_dialog.py
P069-P073 → services/timer_service.py, services/notification_service.py
P074     → 全局测试与打包
```

## 扩展示例

添加新视图类型（如年视图）：新建 `views/calendar/year_view.py`，继承 `BaseCalendarView`，实现三个抽象方法，在 `CalendarHeader` 中添加入口按钮。

添加新通知渠道（如邮件）：在 `NotificationService._create_notification()` 中扩展，无需修改其他模块。
