from collections import deque

incoming = [f"INC-{i:03d}" for i in range(1, 16)]
queue = deque()
MAX_QUEUE = 8
MAX_ACTIVE = 3
active = []
rejected = []

for incident in incoming:
    if len(queue) + len(active) >= MAX_QUEUE + MAX_ACTIVE:
        rejected.append(incident)
    elif len(active) < MAX_ACTIVE:
        active.append(incident)
    else:
        queue.append(incident)

print("Active:", active)
print("Queued:", list(queue))
print("Rejected/load-shed:", rejected)
print("Backpressure protects downstream capacity instead of accepting infinite work.")
