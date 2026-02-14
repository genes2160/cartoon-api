# 🎭 Cartoonizer API — Privacy-Preserving Media Transformation (Research POC)

A **simple FastAPI service** that converts a user-uploaded image into a cartoon/anime style version.

The goal is not entertainment filters —
the goal is **identity abstraction**.

This project explores how visual media can be shared publicly **without exposing real facial identity**, while still keeping human expression, emotion and communication intact.

---

## 🧠 The Idea

In many regions (journalism, education, activism, social commentary, public blogging), people want to speak — but not be visually identifiable.

Blurring faces removes emotion.
Masks look artificial.
Voice-only removes presence.

Cartoonization preserves:

* expression
* gestures
* storytelling
* human connection

while reducing biometric recognizability.

This allows:

* blogging
* vlogging
* tutorials
* commentary
* educational content

without directly exposing the individual.

---

## 🎯 Problem Being Explored

Modern platforms strongly encourage visual presence.
However not everyone can safely publish their real face due to:

* professional boundaries
* safety concerns
* social pressure
* cultural context
* research anonymity
* whistleblowing scenarios
* early-stage creators testing ideas

This tool explores a middle ground:

> Be present without being identifiable.

---

## 🔬 Research Purpose

This repository is a **research prototype** studying:

* personality preservation after visual abstraction
* audience perception of non-realistic avatars
* privacy vs authenticity trade-off
* feasibility of anonymized video blogging

Future direction:

> Real-time video cartoonization for full vlog pipelines

---

## 🔐 Data Protection & Privacy

This application is intentionally designed to be privacy-first.

**Key properties**

* No database
* No file persistence beyond processing
* No external API calls after model download
* Runs fully offline
* Images processed locally only
* No biometric storage
* No training on user data

The system aligns with principles found in privacy frameworks such as:

* GDPR data minimization
* purpose limitation
* local processing
* non-retention

This is a transformation tool — not an identity collection system.

---

## 🏗 Architecture

Client → Upload Image → Local Processing → Return Cartoon Image

No background workers
No analytics
No tracking

---

## 🚀 Setup

### 1. Clone

```bash
git clone <repo>
cd cartoon-api
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Run server

```bash
uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

Upload an image → receive cartoon output.

---

## 📁 Important Git Note

Generated folders must **NOT be committed**

Add to `.gitignore`:

```
uploads/
__pycache__/
*.pt
*.pth
*.onnx
```

Why:

* contains user media
* contains downloaded model weights
* environment specific
* prevents accidental data leakage

---

## 📦 Offline Behaviour

First run:

* model downloads once

Afterwards:

* system works completely offline

This makes the project suitable for:

* unstable connectivity environments
* field research
* controlled local deployments

---

## 🔮 Planned Research Extensions

* video stream cartoonization
* live webcam anonymization
* emotion retention testing
* speech + avatar publishing workflow
* automated vlog publishing pipeline

---

## ⚠ Disclaimer

This project is provided strictly for:

> research, privacy exploration and educational experimentation.

It is **not intended** to bypass platform policies, impersonate individuals, or deceive viewers.

Users are responsible for ethical and lawful usage.

---

## 📜 License

Research / experimental usage recommended.

---