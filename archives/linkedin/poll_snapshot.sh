#!/bin/sh
# Poll the Member Snapshot API until the slow domains (posts, comments, likes,
# votes, reposts) finish processing, fetching everything in the --content set
# each pass. Stops once MEMBER_SHARE_INFO (your posts) has landed.
#
#   nohup sh poll_snapshot.sh > poll_snapshot.log 2>&1 &
#
cd "$(dirname "$0")" || exit 1

max=72          # ~24h at 20 min spacing
interval=1200

i=0
while [ "$i" -lt "$max" ]; do
    i=$((i + 1))
    echo "[poll $i/$max $(date '+%Y-%m-%d %H:%M')] fetching --content domains"
    python3 fetch_member_snapshot.py --content
    if [ -f snapshot/MEMBER_SHARE_INFO.json ]; then
        echo "[poll] MEMBER_SHARE_INFO is ready — stopping."
        exit 0
    fi
    echo "[poll] not ready yet; sleeping ${interval}s"
    sleep "$interval"
done

echo "[poll] gave up after $max attempts"
exit 1
