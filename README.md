# 🛡️ AI Cybersecurity Incident Analysis Agent

An AI-powered cybersecurity incident analysis application that uses
**RAG, FAISS, LangGraph, Gemini, FastAPI, Streamlit, and Pydantic**
to analyze cybersecurity incidents and provide structured defensive
recommendations.

---

## 📌 Project Overview

Cybersecurity analysts often need to analyze large amounts of incident
information and identify the possible type, severity, evidence, and
appropriate defensive actions.

This project provides an AI-based assistant that accepts a
text-based cybersecurity incident description and generates a
structured incident analysis using a cybersecurity knowledge base.

The system uses Retrieval-Augmented Generation (RAG) to retrieve
relevant cybersecurity information before sending the incident and
context to the Gemini language model.

---

## 🎯 Problem Statement

The objective of this project is to build an AI-powered cybersecurity
incident analysis agent that can analyze a given cybersecurity incident
and provide:

- Incident type
- Severity
- Threat explanation
- Evidence
- Recommended defensive actions

The application is designed to support cybersecurity analysts with
initial incident analysis.

---

## 🎯 Objectives

1. Accept cybersecurity incidents as text input.
2. Retrieve relevant cybersecurity knowledge using RAG.
3. Use FAISS for vector similarity search.
4. Use LangGraph to manage the analysis workflow.
5. Use Gemini for incident analysis.
6. Generate structured output using Pydantic.
7. Provide a FastAPI backend.
8. Provide a Streamlit user interface.
9. Provide defensive cybersecurity recommendations.

---

## 🏗️ System Architecture

```text
                User
                  │
                  ▼
          ┌───────────────┐
          │   Streamlit   │
          │      UI       │
          └───────┬───────┘
                  │
                  ▼
          ┌───────────────┐
          │    FastAPI    │
          └───────┬───────┘
                  │
                  ▼
          ┌───────────────┐
          │   LangGraph   │
          └───────┬───────┘
                  │
             ┌────┴─────┐
             │          │
             ▼          ▼
        Retrieve      Analyze
             │          │
             ▼          ▼
           FAISS      Gemini
             │          │
             └────┬─────┘
                  │
                  ▼
          ┌───────────────┐
          │   Pydantic    │
          │    Output     │
          └───────┬───────┘
                  │
                  ▼
          Incident Analysis