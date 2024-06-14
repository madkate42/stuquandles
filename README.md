# Polynomial Invariant of Stuck Knots

## Installation

To set up this project, clone the repository to your local machine by running:

```bash
git clone https://github.com/madkate42/stuquandles.git
cd stuquandles
```

You must have Python 3 installed on your system to run the programs in this repository. 
No additional packages are needed to run this project. For instructions on how to download and install Python, please visit the [Python Beginner's Guide](https://wiki.python.org/moin/BeginnersGuide/Download).

## 1. Try a stuquandle on the links

In the file `links.py`, make tables that represent * operation (q), R1, R2, R3, R4. Then, run
```bash
python3 links.py
```
In the output, you will see the counting invariant, the colorings, whether they are the same for both links, and the substuquandle polynomials.

## 2. Test whether a collection of tables represent a stuquandle BASED ON THE TABLES

In the file `is_stuquandle.py`, change the operation tables q (*), R1, R2, R3, R4 to yours. Then, run
```bash
python3 is_stuquandle.py
```
Then, it'll output True/False!

## 3. Test whether a stuquandle BASED ON ALGEBRAIC EXPRESSIONS

In the file `is_stuquandle_ops.py`, change your n on line 4 and on every line where it says "CHANGE THE NEXT LINE ACCORDING TO YOUR OPERATION", change the line that starts with `value = ` based on your algebraic expression for each operation (op is *), R1, R2, R3, R4. Run:
```bash
python3 is_stuquandle.py
```
Then, it'll output the tables and True/False!