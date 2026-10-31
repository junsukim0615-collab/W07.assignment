"""Display saved Task 2 measurements and ARP capture analysis in VS Code."""
from pathlib import Path
import subprocess
import re

OUT = Path(__file__).resolve().parent / 'out'
def read(name):
    path = OUT / name
    return path.read_text(encoding='utf-8-sig', errors='replace') if path.exists() else '(not recorded)'

def main():
    sections = []
    def show(title, value):
        print('\n' + title + '\n' + value, flush=True)
        sections.append('## ' + title + '\n\n```text\n' + value + '\n```\n')
    show('ARP BEFORE', read('arp-before.txt'))
    show('ARP IMMEDIATELY AFTER CLEAR', read('arp-immediate.txt'))
    show('GATEWAY PING', read('ping-gateway.txt'))
    show('WEB ACCESS', read('web-access.txt'))
    show('ARP AFTER', read('arp-after.txt'))
    def dynamic_count(text):
        # Only compare the active Wi-Fi interface, excluding VMware/static entries.
        match = re.search(r'Interface: 192\.168\.219\.178.*?(?=Interface:|\Z)', text, re.S)
        return len(re.findall(r'\bdynamic\b', match.group(0))) if match else None
    before, after = dynamic_count(read('arp-before.txt')), dynamic_count(read('arp-after.txt'))
    show('WI-FI DYNAMIC ENTRY COUNTS', f'before={before}, after={after}')
    cap = OUT / 'arp.pcapng'
    if cap.exists():
        cmd = [r'C:\Program Files\Wireshark\tshark.exe', '-r', str(cap), '-Y', 'arp', '-T', 'fields', '-E', 'separator=,', '-e', 'frame.time_relative', '-e', 'eth.src', '-e', 'eth.dst', '-e', 'arp.opcode', '-e', 'arp.src.proto_ipv4', '-e', 'arp.dst.proto_ipv4']
        result = subprocess.run(cmd, capture_output=True, text=True)
        rows = result.stdout.strip().splitlines() if result.stdout.strip() else []
        own_rows = [row for row in rows if '192.168.219.178' in row]
        show('MY ARP REQUEST/REPLY (seconds,srcMAC,dstMAC,opcode,srcIP,dstIP)', '\n'.join(own_rows) or result.stderr)
        show('ARP COUNT', f'{len(rows)} ARP packets in the configured 60-second capture.\nExample estimate for 1000 machines: {len(rows)} x 1000 = {len(rows)*1000} packets/min.\nThis is a rough arithmetic estimate; shared broadcasts and traffic differences prevent linear prediction.')
    (OUT / 'task2-measurement-results.md').write_text('# Task 2 measurement results\n\n' + '\n'.join(sections), encoding='utf-8')

if __name__ == '__main__':
    main()
    print('\n' + read('task2-analysis.md'), flush=True)

