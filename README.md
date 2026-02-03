# Indonesian Deception Detection Dataset - Code Repository

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Dataset DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.17421590-blue)](https://doi.org/10.5281/zenodo.17421590)

This repository contains the complete code for feature extraction, preprocessing, quality validation, and baseline classification used in:

**"Indonesian Deception Detection Dataset of Video-Based Testimonial Recordings with Personality Assessment Across Six Ethnic Groups"**

*Published in Scientific Data (2025)*

---

## 📊 Dataset Access

The complete dataset (1,568 video recordings, multimodal features) is publicly available at:

**Zenodo:** https://doi.org/10.5281/zenodo.17421590

**Dataset includes:**
- 🎤 Audio features (94 acoustic features, preprocessed WAV files)
- 👁️ Visual landmarks (468 facial, 10 iris, 33 pose landmarks per frame)
- 📝 Text features (Indonesian transcripts with English translations)
- 🧠 Personality assessments (DISC profiles)
- 🌏 Six Indonesian ethnic groups (Javanese, Sundanese, Madurese, Bugis-Makassar, Batak, Minangkabau)

---

## 📂 Repository Structure
Indonesian-Deception-Detection-Dataset/
├── baseline_validation/      # Baseline model validation scripts
├── figures/                   # Visualization outputs
├── metadata/                  # Dataset metadata and documentation
├── validation/                # Quality validation results
│
├── 01. Dataset_konsistensiCheck.ipynb              # Dataset consistency checks
├── 01. Feature_extraction_I3D_full.ipynb           # I3D feature extraction (full dataset)
├── 01. Feature_extraction_I3D_lie.ipynb            # I3D feature extraction (deceptive samples)
├── 01. Feature_extraction_I3D_truth.IPYNB          # I3D feature extraction (truthful samples)
├── 01. Feature_extraction_I3D_lie_truth_merge.ipynb # Merge lie and truth features
├── 01. Feature_extraction_RLT.ipynb                # Real-Life Trial dataset processing
├── 01. QC_Feature_extraction.ipynb                 # Quality control for feature extraction
├── 02. Baseline_validation.ipynb                   # Baseline classification models
├── envirom.ipynb                                   # Environment verification
│
├── config_I3D.yaml            # Configuration for I3D dataset processing
├── config_RLT.yaml            # Configuration for RLT dataset processing
├── landmark_annotations.py    # Landmark annotation utilities
├── environment_verification_report.json  # System environment report
│
├── LICENSE                    # MIT License
└── README.md                  # This file

