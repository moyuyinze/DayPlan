-- DayPlan 初始数据库迁移
-- 版本: 001

CREATE TABLE IF NOT EXISTS db_version (
    version     INTEGER PRIMARY KEY,
    applied_at  TEXT NOT NULL DEFAULT (datetime('now', 'localtime'))
);

-- 分类表
CREATE TABLE IF NOT EXISTS categories (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT NOT NULL UNIQUE,
    color       TEXT NOT NULL DEFAULT '#4A90D9',
    icon        TEXT DEFAULT '',
    sort_order  INTEGER NOT NULL DEFAULT 0,
    created_at  TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
    updated_at  TEXT NOT NULL DEFAULT (datetime('now', 'localtime'))
);

-- 日程主表
CREATE TABLE IF NOT EXISTS schedules (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    title           TEXT NOT NULL,
    description     TEXT DEFAULT '',
    location        TEXT DEFAULT '',
    start_time      TEXT NOT NULL,
    end_time        TEXT NOT NULL,
    is_cross_day    INTEGER NOT NULL DEFAULT 0,
    category_id     INTEGER DEFAULT NULL,
    priority        INTEGER NOT NULL DEFAULT 0,
    repeat_type     TEXT NOT NULL DEFAULT 'none',
    repeat_interval INTEGER NOT NULL DEFAULT 1,
    repeat_end_date TEXT DEFAULT NULL,
    notify_before   INTEGER DEFAULT NULL,
    deadline_notify INTEGER NOT NULL DEFAULT 0,
    is_completed    INTEGER NOT NULL DEFAULT 0,
    total_duration  INTEGER NOT NULL DEFAULT 0,
    created_at      TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
    updated_at      TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE SET NULL
);

CREATE INDEX IF NOT EXISTS idx_schedules_start ON schedules(start_time);
CREATE INDEX IF NOT EXISTS idx_schedules_category ON schedules(category_id);
CREATE INDEX IF NOT EXISTS idx_schedules_completed ON schedules(is_completed);

-- 重复日程例外表
CREATE TABLE IF NOT EXISTS schedule_exceptions (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    schedule_id     INTEGER NOT NULL,
    exception_date  TEXT NOT NULL,
    FOREIGN KEY (schedule_id) REFERENCES schedules(id) ON DELETE CASCADE,
    UNIQUE(schedule_id, exception_date)
);

-- 计时记录表
CREATE TABLE IF NOT EXISTS timer_records (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    schedule_id   INTEGER NOT NULL,
    started_at    TEXT NOT NULL,
    ended_at      TEXT DEFAULT NULL,
    duration      INTEGER DEFAULT 0,
    FOREIGN KEY (schedule_id) REFERENCES schedules(id) ON DELETE CASCADE
);

-- 应用设置表
CREATE TABLE IF NOT EXISTS app_settings (
    key           TEXT PRIMARY KEY,
    value         TEXT NOT NULL,
    updated_at    TEXT NOT NULL DEFAULT (datetime('now', 'localtime'))
);
