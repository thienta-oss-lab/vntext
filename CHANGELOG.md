# Changelog

All notable changes to this project are documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Fixed

- `remove_accents` now converts `đ`/`Đ` to `d`/`D`, so `slugify` no longer drops them.

## [0.1.0] - 2026-11-14

### Added

- `remove_accents`, `slugify` and `to_words`.
