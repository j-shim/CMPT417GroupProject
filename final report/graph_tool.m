a_star_path = [20,6,16,20,22,22,8,16,14,20];
ida_path = [20,6,16,20,22,22,8,16,14,20];
bfs_path = [20,6,16,20,22,22,8,16,14,20];
dfs_path = [71872,2572,25672,42200,67072,104046,43650,11256,88506,7730];
iddfs_path = [32,6,16,40,46,26,10,26,14,26];

a_star_time = [3.64,0.02,0.19,2.27,20.95,25.08,0.03,0.24,0.14,3.59];
ida_time = [2.36,0.01,0.2,1.61,11.17,11.13,0.03,0.29,0.2,2.49];
bfs_time = [10.9,0.04,1.76,8.76,28.52,24.45,0.08,2.23,0.83,14.81];
dfs_time = [19.32,0.57,5.54,9.49,17.29,33.11,11.24,2.94,24.45,1.96];
iddfs_time = [129.95,0.06,7.36,6.88,16.48,47.55,0.32,3.43,0.93,33.14];

a_star_node = [2873,14,383,2459,8198,8142,31,427,239,2842];
ida_node = [10818,28,1107,8866,52456, 43599,62,1362,690,11509];
bfs_node = [53062,102,10061,50185,147980,147883,271,10529,3914,60085];
dfs_node = [128273,2993,36381,93662,217951,261183,45257,22033,97911,67983];
iddfs_node = [645351,369,70925,134708,298923,458185,46766,34525,102848,198838];

a_star_mem = [3.466045,0.019211,0.430408,2.984379,10.125561,10.111702,0.039004,0.486992,0.301032,3.415359];
ida_mem = [0.046734,0.011848,0.035069,0.043926,0.046986,0.049778, 0.015846,0.035046,0.029903,0.044651];
bfs_mem = [29.251396,0.061516,7.054901,28.958473,52.433998,55.09515,0.174217,7.23516,2.492794,31.156795];
dfs_mem = [63.70071,2.205161,22.597842,37.515369,60.470665,84.693793,38.569678,10.007056,74.813816,7.201175];
iddfs_mem = [26.891144,0.040268,3.770847,3.057194,5.497227,13.483478,0.18391,1.293933,0.430725,7.2461];


A = [mean(a_star_path),mean(ida_path),mean(bfs_path),mean(dfs_path),mean(iddfs_path)];
B = [mean(a_star_time),mean(ida_time),mean(bfs_time),mean(dfs_time),mean(iddfs_time)];
C = [mean(a_star_mem),mean(ida_mem),mean(bfs_mem),mean(dfs_mem),mean(iddfs_mem)];
mean_node = [mean(a_star_node),mean(ida_node),mean(bfs_node),mean(dfs_node),mean(iddfs_node)];

figure(1)
histogram('Categories',{'A*','IDA*','BFS','DFS','IDDFS'},'BinCounts',A)
ylim([0,150]);
title('Efficiency histogram of different algorithms')
hold on
bar(B,'BarWidth',0.7);
bar(C,'BarWidth',0.5);
legend('mean path length','mean time cost','mean memory usage','Location','northwest')
hold off

figure(2)
histogram('Categories',{'A*','IDA*','BFS','DFS','IDDFS'},'BinCounts',mean_node)
legend('mean expanded nodes','Location','northwest')
title('Expanded nodes of different algorithms')

figure(3)
plot(a_star_time,'-o');
hold on
plot(ida_time,'-o');
plot(bfs_time,'-o');
plot(dfs_time,'-o');
plot(iddfs_time,'-o');
legend('A*','IDA*','BFS','DFS','IDDFS');
title('Time cost on 10 puzzles')
hold off

figure(4)
plot(a_star_mem,'-o');
hold on
plot(ida_mem,'-o');
plot(bfs_mem,'-o');
plot(dfs_mem,'-o');
plot(iddfs_mem,'-o');
legend('A*','IDA*','BFS','DFS','IDDFS');
title('Memory usage on 10 puzzles');
hold off