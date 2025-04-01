# 18352번: 특정 거리의 도시 찾기 - <img src="https://static.solved.ac/tier_small/9.svg" style="height:20px" /> Silver II

<!-- performance -->

<!-- 문제 제출 후 깃허브에 푸시를 했을 때 제출한 코드의 성능이 입력될 공간입니다.-->

<!-- end -->

## 문제

[문제 링크](https://boj.kr/18352)


<p>어떤 나라에는 1번부터 <em>N</em>번까지의 도시와&nbsp;<em>M</em>개의 단방향 도로가 존재한다. 모든 도로의 거리는 1이다.</p>

<p>이 때 특정한 도시 <em>X</em>로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 <em>K</em>인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오.&nbsp;또한 출발 도시 <em>X</em>에서 출발 도시 <em>X</em>로 가는 최단 거리는&nbsp;항상 0이라고 가정한다.</p>

<p>예를 들어 <em>N</em>=4, <em>K</em>=2, <em>X</em>=1일 때 다음과 같이 그래프가 구성되어 있다고 가정하자.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/a5e311d7-7ce4-4638-88a5-3665fb4459e5/-/preview/" style="height: 249px; width: 250px;"></p>

<p style="text-align: justify;">이 때 1번 도시에서 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 2인 도시는 4번 도시 뿐이다. &nbsp;2번과 3번 도시의 경우, 최단 거리가 1이기 때문에 출력하지 않는다.</p>



## 입력


<p>첫째 줄에 도시의 개수 <em>N</em>,&nbsp;도로의 개수 <em>M</em>, 거리 정보 <em>K</em>, 출발 도시의 번호 <em>X</em>가 주어진다. (2 ≤&nbsp;<em>N&nbsp;</em>≤ 300,000, 1 ≤&nbsp;<em>M&nbsp;</em>≤ 1,000,000, 1 ≤&nbsp;<em>K&nbsp;</em>≤ 300,000, 1 ≤&nbsp;<em>X&nbsp;</em>≤&nbsp;<em>N</em>) 둘째 줄부터 <em>M</em>개의 줄에 걸쳐서 두 개의 자연수 <em>A</em>, <em>B</em>가 공백을 기준으로 구분되어 주어진다. 이는 <em>A</em>번 도시에서 <em>B</em>번 도시로 이동하는 단방향 도로가 존재한다는 의미다. (1 ≤&nbsp;<em>A</em>, <em>B&nbsp;</em>≤&nbsp;<em>N</em>) 단, <em>A</em>와 <em>B</em>는 서로 다른 자연수이다.</p>



## 출력


<p><em>X</em>로부터 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 <em>K</em>인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력한다.</p>

<p>이 때 도달할 수 있는 도시 중에서, 최단 거리가 <em>K</em>인 도시가 하나도 존재하지 않으면 -1을 출력한다.</p>



## 소스코드

[소스코드 보기](특정%20거리의%20도시%20찾기.py)