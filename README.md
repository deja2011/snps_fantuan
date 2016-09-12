# SNPS Yuefan

----

## Active AIs
- Details 显示joined person list -- Yimin (Done)

- MyTuan显示 joined tuan list -- Yimin (Done)

- Details 专门开一个column -- Lawrence (Skipped)

- Navigator 做成模板 -- Lawrence (Done)

- Celery部署 -- Yimin

- MyTuan table 显示bug -- Zoe (Done)

- Authenticate decorator -- Leo (Done)
  - Logic enhancement -- Leo:
      1. no duplicate join

- Change to datatime to all table -- Jessie

- Use form view in my Tuan view -- Lawrence

- Login redirect might have bug. Cannot reproduce during meeting. -- Yimin (Done)

- db switch/population -- Lawrence (Done. population will be skipped for now.)

----

## Database Setup
###### Lawrence @ 2016/09/09
Following three files will be excluded from Git repository.
- `tuanproj/settings_local.py`
- `db.sqlite3`
- `django.db`

The default database is setup in `tuanproj/settings.py` and points to Leo's MySQL at `pvicc015:python_django`. To use this database, make sure `tuanproj/settings_local.py` doesn't exist, or this local setup file doesn't overwrite default database setup. Alternatively, to use custom database for local test, please place related setup in `tuanproj/settings_local.py`.

An example `settings_local.py` is at `tuanproj/settings_local.example.py`.
