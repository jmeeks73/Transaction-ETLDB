--1. Create Database

CREATE DATABASE TransactionETLDB;
GO

--2. Create Table

CREATE TABLE dbo.transaction_raw (
    transaction_id                 VARCHAR(50),
    sender_account_id              VARCHAR(50),
    receiver_account_id            VARCHAR(50),
    transaction_amount             DECIMAL(12,2),
    transaction_type               VARCHAR(50),
    timestamp                      DATETIME,
    transaction_status             VARCHAR(50),
    fraud_flag                     BIT,
    geolocation_latitude_longitude VARCHAR(100),
    device_used                    VARCHAR(50),
    network_slice_id               VARCHAR(50),
    latency_ms                     INT,
    slice_bandwidth_mbps           INT,
    pin_code                       INT
);
GO

