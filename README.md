# InvoiceReaderProject
This repository contains scripts and other documents for our project in Unternehmenssoftware

## Members
- Omid
- Duncan
- Jerome

## Goals

### Primary

Our primary goal is to build a classification model to identify a variety of different invoices

### Secondary

Our secondary goal is to build a ruleset for each invoice to read / extract specific it's data

## Project Planning

### Active Tasks
1. Build Classification Mode **[Jerome]** -> ~~*Tensorflow*~~ *OCR*
2. Build Rule Sets for Invoices (Name, Address, Invoice Date, Amount €) **[Omid, Duncan]** -> *OCR (pytesseract)*

### Invoice Data Generation
1. Select invoice (Amazon, Apple, Xing, ...)
2. Create template (.docx)
3. Write script for invoice generation
4. Create data frames (Person, Product) with pseudo data
5. Generate invoice pdf files
6. Convert invoice files to .png files

### Simulation Prep
1. Build Classification Model
2. Create / Modify ruleset(s)
3. Create test-data set(s) + create training-data set(s)

### Simulation
- Run Test with **2** invoice types
- Run Test with **3** invoice types 
- [...]
### Analysis
- How does the performance change with each added invoice type?
- How is the accuracy overall?
- What could be improved?
