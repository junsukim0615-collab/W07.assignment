# W07.assignment

컴퓨터네트워크 7주차 학습 스위치 및 ARP 실측 과제입니다.

## Task 1

- [구현 코드](w07-ethernet-arp/task1_switch.py)
- [검증 결과](w07-ethernet-arp/out/task1-result.md): 제공된 7개 검사 통과

## Task 2

- [실측 분석 및 요구사항 답변](w07-ethernet-arp/out/task2-analysis.md)
- [삭제 전 ARP 테이블](w07-ethernet-arp/out/arp-before.txt)
- [복원 후 ARP 테이블](w07-ethernet-arp/out/arp-after.txt)
- [ARP 캡처](w07-ethernet-arp/out/arp.pcapng): 내 PC 관련 요청·응답 4개(2쌍)
- [1분 측정 요약](w07-ethernet-arp/out/arp-minute-summary.txt): 원본 139개, 제출본은 다른 장치 대상 요청 제외
- [검사 결과](w07-ethernet-arp/out/task2-test.txt): 4 passed, 0 failed, 0 skipped
- [관찰 기록](w07-ethernet-arp/out/observation.md)

```bash
cd w07-ethernet-arp
python task1_switch.py --verify
python test_tasks.py --task 1
python test_tasks.py --task 2
```

Task 2 캡처 내용 검사에는 tshark가 필요합니다. `task2_show_results.py`는 저장된 실측 자료를 표시하는 보조 스크립트이며 현재 Windows 설치 경로와 실험 당시 주소를 기준으로 작성했습니다. 제출용 캡처로 다시 실행하면 패킷 수는 4개로 표시됩니다. 원본 1분 측정값 139개는 별도 측정 요약을 참고하세요.

## Task 3

- [구현 코드](w07-ethernet-arp/task3_flooding.py)
- [비교 분석](w07-ethernet-arp/out/task3-analysis.md)
- [벤치마크 출력](w07-ethernet-arp/out/bench.txt)
- [검사 결과](w07-ethernet-arp/out/task3-test.txt)

불필요한 전달 323,380 → 156,814회(51.51% 감소), 정상 전달 46,347회, 누락 0회로 strong 기준을 충족했다. bench.py는 과제 원본과 동일하다. 관찰문에는 교체 기준, 새 항목 수용 비교, 공격과 방어를 기록했다.

```bash
python bench.py --yours
python test_tasks.py --task 3
```

Task 3 자동 검사에서 공격 설명은 사람이 평가하므로 skip으로 표시된다.

과제 원본: https://github.com/codingchild2424/2026-lecture-network-practice/tree/main/w07-ethernet-arp
