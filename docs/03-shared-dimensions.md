# Shared dimensions

## Overview

These dimensions are conformed across Operations. Every enterprise dashboard must offer **Channel**. Do not create Channel-siloed copies of the same metric.

Grain notes tell you what a row in the dimension means. “Do not confuse with” stops the usual collisions (marketing channel vs Channel, occupancy of property vs Waiting-on party, funding vs purchase).

Time zone for Event date and As-of is the **company operations calendar**. Until leadership names it, treat that as the LOS business timezone and label it on every dashboard. Do not silently mix application date, lock date, and Funded date.

## Enterprise filters (always available)

| Dimension | Definition | Grain | Do not confuse with |
|-----------|------------|-------|---------------------|
| Channel | Retail, Wholesale, or Correspondent | Loan file | Marketing channel, lead source |
| Correspondent authority | Delegated vs non-delegated (who underwrote at the TPO). Use on P09 when the company has both. | Loan file (Corr) | Channel; TPO name |
| Loan purpose | Purchase, rate/term refinance, cash-out refinance, streamline/IRRRL | Loan file | Product program |
| Product program | Conventional, FHA, VA, USDA, jumbo, non-QM, other | Loan file | Investor (a conventional loan can deliver to more than one investor) |
| Occupancy | Primary, second home, investment | Loan file | Waiting-on party |
| Property type | Site-built, condo, PUD, manufactured, 2–4 unit, other | Loan file | |
| State | Property state | Loan file | Fulfillment center location |
| Investor | Committed or likely investor | Loan file | Product program; Channel |
| Commitment | Specific investor commitment or pool when assigned | Loan file | Lock |
| Current milestone | Manufacturing stage the file is in at As-of | Loan file As-of | Lock status, AUS recommendation, condition status |
| Fulfillment center / pod / team | Internal manufacturing team | Loan file | Branch (Retail sales org) |
| Lock status | Locked, expired, not locked, float | Loan file As-of | Lock price, note rate (Capital Markets) |
| Event date | Date the measured event occurred | Event | As-of date; application date used as a silent substitute |
| As-of date | Snapshot date for Pipeline, aging, locks in force | Snapshot | Event date |

## People and organization

| Dimension | Definition | Grain | Do not confuse with |
|-----------|------------|-------|---------------------|
| Loan officer | Retail originating salesperson | Loan file | Processor; Broker |
| Branch | Retail sales branch | Loan file | Fulfillment center |
| Broker | Wholesale originating company | Loan file | TPO; Vendor |
| TPO | Correspondent seller company | Loan file | Broker; Vendor |
| Processor | Assigned processor (current, and originating if different) | Loan file | Underwriter |
| Underwriter | Assigned UW (current, and decisioning UW) | Loan file | QC reviewer |
| Closer | Assigned closer | Loan file | Post-closer |
| Post-closer | Assigned post-close owner | Loan file | Closer |
| Manager / team | Roll-up of the role above | Team | Fulfillment center when they differ |

**Rule:** Productivity metrics credit the **completing assignee** on the event date. Aging metrics use the **current assignee** at As-of.

## File characteristics (bands, not raw PII)

| Dimension | Definition | Notes |
|-----------|------------|-------|
| Loan amount band | Company bands on note amount (or purchase amount for Correspondent) | Use the same bands on Funded and Correspondent purchase |
| LTV / CLTV band | Combined LTV bands | |
| FICO band | Representative credit score bands | |
| Units | 1 unit vs 2–4 | |
| Income type | W2 vs self-employed vs other | Drives processing Cycle time |
| AUS recommendation | Approve/Eligible, Refer, Ineligible, Out of Scope, other | Not an UW decision |
| Waiting-on party | Borrower, Broker/TPO, Vendor, internal | First-class aging slice |
| Occupancy of milestone | Same as Waiting-on party; do not add a second name | Canonical name is Waiting-on party |

## Vendor and order

| Dimension | Definition | Grain |
|-----------|------------|-------|
| Vendor type | AMC, appraiser, title, closing attorney, credit, flood, tax, QC vendor | Order |
| Vendor name | Conformed panel name | Order |
| Order type | Appraisal, title, flood, credit, tax, MI, other | Order |
| Appraisal path | Company-ordered, Broker-ordered, transferred, waived, seller (Correspondent) | Loan file / order |

TPO and Broker are **not** Vendor names. TPO scorecards live on D08/D11.

## Time

| Dimension | Definition |
|-----------|------------|
| Event date | Date of Funded, decision, Delivered, etc. |
| As-of datetime | Pipeline snapshot; recommend 6:00 a.m. ops-calendar |
| Business-day calendar | Company holidays for Cycle time |
| Calendar day | TRID clocks only (D14 and CD timing notes on D07) |
| Cohort month | Start month, lock month, or submission month for Pull-through — the metric name says which |

## Explicit non-dimensions (do not add to Operations views)

| Field | Belongs in |
|-------|------------|
| Marketing channel, lead provider, CPL, ROM, lead spend | Sales |
| Note rate, lock price, gain-on-sale, hedge | Capital Markets |
| Delinquency, escrow shortage, call-center reason | Servicing |
| Independent audit QC sample flag (unless dual-tagged) | Quality |

## Filter defaults

| Dashboard class | Default Channel | Default date |
|-----------------|-----------------|--------------|
| D01 Command Center | All channels | Last complete week plus MTD, both labeled |
| D07 Closing and funding | Retail + Wholesale (Correspondent off) | Event date = Funded date |
| D08 Correspondent operations | Correspondent only | Event date = Submission or purchase date, labeled |
| D14 Disclosures | Retail + Wholesale | Calendar days; Event date = LE sent |
| All others | All channels | Ops calendar; Event vs As-of labeled on each KPI |
