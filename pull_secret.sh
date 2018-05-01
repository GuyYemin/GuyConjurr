#! /bin/bash -e
function main() {
  echo "-----"
  fetch_secret
}

function fetch_secret() {
	local X=$(conjur variable value jenkins/github/username)
	echo "Secret=$X" 
}

main