#!/bin/bash
function test1 () {
    local MESSAGE="Hello World!"
    echo $MESSAGE
}

echo "hello world!"

MESSAGE="test12345"
echo $MESSAGE
test1
echo $MESSAGE