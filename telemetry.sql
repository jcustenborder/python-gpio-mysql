create database if not exists telemetry;
use telemetry;

/*
Create a user named telemetry that can be accessed from any('%') host. We could use this
to restrict where this account could be used. For example localhost would mean the same host.
 */

CREATE USER if not exists 'telemetry'@'%' IDENTIFIED BY 'xldfbgsdbfbladfvasd';
GRANT ALL PRIVILEGES ON *.* TO 'telemetry'@'%';

drop table if exists telemetry;

/*
 Rename the sensor fields to be contextual.
 */

create table telemetry (
    timestamp timestamp not null,
    sensor1 double precision,
    sensor2 double precision,
    sensor3 double precision,
    sensor4 double precision
);

/*

 */