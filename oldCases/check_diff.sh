#!/bin/bash

# check_diff.sh
# Usage: ./check_diff.sh expected.txt output.txt

EXPECTED="$1"
OUTPUT="$2"

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 expected_file output_file"
    exit 1
fi

# Check if both files exist
if [ ! -f "$EXPECTED" ]; then
    echo "Error: Expected file '$EXPECTED' does not exist."
    exit 1
fi

if [ ! -f "$OUTPUT" ]; then
    echo "Error: Output file '$OUTPUT' does not exist."
    exit 1
fi

# Compare files with unified diff
if diff -u <(xxd "$EXPECTED") <(xxd "$OUTPUT") > diff_result.txt; then
    echo "✅ Test Passed"
    rm diff_result.txt
else
    echo "❌ Test Failed - Differences found:"
    cat diff_result.txt
fi