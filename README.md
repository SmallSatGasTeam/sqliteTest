# Testing the Viability of SQLite333 for Orbital Systems
Scott Glaittli

## Abstract

## Methods
The experiment was run using a Raspberry pi 3B+ and Python 3.8.  Following are the specifications for the computer used to run the experiment:

- OS: Raspbian 10 buster
- Kernel: armv7l Linux 4.19.97-v7+
- CPU: ARMv7 rev4 (v7l) @ 1.2GHz
- RAM: 106MiB / 874MiB

TODO: Also run tests on the Raspberry Pi Zero

Using Python's sqlite3 module, the time performance was measured using the Python datetime module which has accuracy on the nanosecond scale.  The following tests were performed:
1. The time taken to connect to the SQLite3 database
2. The time taken to create a table 30 columns wide of text type entries in the SQLite3 database 
3. The time taken to insert a single row of random text to the table
4. The time taken to insert the entire Raspberry Pi system dictionary to the text table (~50,000 words formatted into rows 30 wide)
5. The time taken to select all data in the database
6. The time taken to select all rows in the database where the first letter of the word in the first column is an "a" or an "A"
7. The time taken to insert XXX random unix time stamps into a table in the database
8. The time taken to select all rows from the timestamp table
9. The time taken to select various ranges of data from the timestamp table

## Results

## Conclusion
