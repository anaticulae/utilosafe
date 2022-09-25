# Changelog

Every noteable change is logged here.

## v0.4.2 (2022-09-25)

### Chore

* upgrade Jenkinsfile (55bb40424ac6)
* decrease to working crypto version (8c209977ae91)
* upgrade requirements.txt (14c77c23fc9f)

## v0.4.1 (2022-09-23)

### Fix

* ensure working without Crypto package (4c15cb1ee5f0)

### Chore

* add Jenkinsfile (1beaea444306)
* upgrade requirements.txt (b424d0993ba5)

## v0.4.0

### Feature

* use public key if no key is given (c574e1d96e08)
* use public as a wrapper to may change algo later (0e4e0a16242b)
* adjust interface to new API (340aef366bba)
* use OpenSSL for encryption (6cf7a7920602)

### Fix

* adjust password initialization (5b7a07f3be00)
* new API requires bytes (fcedc98d5d5e)

## v0.3.1

### Fix

* import on runtime (fd9be45f7eca)

### Documentation

* adjust modules path (45cf6e42c58a)
* Happy New Year! (d9ddb6326913)

## v0.3.0

### Feature

* reduce bits to increase speed (f8ffa8843b73)

### Fix

* ensure that DSA is imported (2f279b17138e)
* ensure decrypting large data (63898514bcfd)

## v0.2.0

### Feature

* add environment vars to public API (0a21c86aa6ae)

## v0.1.1

### Fix

* add missing import (c14bdcf9ab08)

## v0.1.0

### Feature

* cache accessing password (e11a168afdce)
* load public password from file of env var (092da1ef6578)
* add cli to generate rsa files (b08c92ab72b0)
* add parameter to encrypt passphrase (986ede720d0e)
* add method to load and write rsa key (6fd3cf41c51f)
* add method to use public/private encryption (de66e5fabb9e)
* add method to generate private and public rsa keys (7026b525809c)
* move utila code (d199552633f0)

## v0.0.0 Initial release
