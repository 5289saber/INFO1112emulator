#!/bin/bash

# Usage: ./testCaseOne.sh testCaseOneExp.txt

EXPECTED=$1
OUTPUT=testCaseOneOut.txt

if [ $# -ne 1 ]; then
  echo "Usage: $0 expected_output.txt"
  exit 1
fi

if [ ! -f "$EXPECTED" ]; then
  echo "Error: Expected output file '$EXPECTED' not found."
  exit 1
fi

# Run the assembler command
python3 assembler.py testing.prog > "$OUTPUT"

# Compare actual vs expected
if diff -u "$EXPECTED" "$OUTPUT" > diff_result.txt; then
  echo "✅ Test Passed"
  rm diffResultOne.txt
else
  echo "❌ Test Failed - Differences found:"
  cat diffResultOne.txt
fi