"""Reproduce the admission-policy comparison without changing bench.py."""
from pathlib import Path
import bench
from task3_flooding import NaiveSwitch, YourSwitch

def main():
    source = Path(__file__).with_name('task3_flooding.py').read_text(encoding='utf-8')
    condition = 'if victim is None or src_count > self.frequency[victim]:'
    if source.count(condition) != 1:
        raise RuntimeError('Admission condition changed; review the comparison.')
    namespace = {}
    exec(compile(source.replace(condition, 'if True:'), '<always-admit comparison>', 'exec'), namespace)
    _, where, frames = bench.build()
    print(f'Seed={bench.SEED}, frames={len(frames)}, capacity={bench.CAPACITY}')
    baseline = bench.run(NaiveSwitch, 'baseline', where, frames)
    always = bench.run(namespace['YourSwitch'], 'always-admit', where, frames)
    selective = bench.run(YourSwitch, 'selective', where, frames)
    assert always['missed'] <= baseline['missed']
    assert selective['missed'] <= baseline['missed']
    print(f"Reduction vs baseline: {100*(1-selective['wasted']/baseline['wasted']):.2f}%")
    print(f"Admission policy saves: {always['wasted']-selective['wasted']} wasted deliveries")

if __name__ == '__main__':
    main()
