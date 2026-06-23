# SmartSort AI

## Overview

SmartSort AI is an offline intelligent file organization system powered by local Large Language Models (LLMs) through Ollama.

The application automatically:

* Monitors incoming files
* Extracts document content
* Classifies files using AI
* Generates meaningful filenames
* Organizes files into category-based folders
* Stores processing history for recovery and auditing

The entire system runs locally without requiring cloud APIs, ensuring privacy and offline functionality.

---

## Architecture

```text
Files
  ↓
Content Extraction
  ↓
Ollama (Local LLM)
  ↓
Classification & Filename Generation
  ↓
File Organization
  ↓
SQLite History
  ↓
Dashboard & Undo
```

---

## Features

* AI-powered document classification
* AI-generated descriptive filenames
* Automatic file organization
* Real-time folder monitoring
* PDF, DOCX, TXT, and image support
* OCR-based text extraction
* SQLite history tracking
* Undo functionality
* Streamlit dashboard
* Fully offline operation using Ollama

---

## Tech Stack

### Core

* Python

### AI

* Ollama
* Gemma / Qwen

### File Monitoring

* Watchdog

### Database

* SQLite

### Dashboard

* Streamlit

### Document Processing

* PyMuPDF
* python-docx

### OCR

* Tesseract OCR
* Pillow

---

## Project Structure

```text
SmartSortAI/
│
├── pipeline.py
├── monitor.py
├── processor.py
├── extractor.py
├── classifier.py
├── renamer.py
├── mover.py
├── database.py
├── undo.py
├── app.py
│
├── uploads/
├── organized/
├── restored/
└── database/
```
