# Add raftos package to PYTHONPATH so we don't need to install it to run example
export PYTHONPATH="${PYTHONPATH}:$(pwd)/../"

# Remove previous data
rm -f *.log
rm -f *.storage
rm -f *.state_machine

# Start
../env/bin/python node.py --node "8000" --cluster "8000 8001 8002 8003" &
../env/bin/python node.py --node "8001" --cluster "8000 8001 8002 8003" &
../env/bin/python node.py --node "8002" --cluster "8000 8001 8002 8003" &
