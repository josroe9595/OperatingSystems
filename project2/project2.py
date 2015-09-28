import operator
import Queue

class cpu_process:
	def __init__(self,proc_num,burst_time,num_bursts,io_time,priority):
		self.name = int(proc_num)
		self.b_time = int(burst_time)
		self.num_b = int(num_bursts)
		self.iotime = int(io_time)
		self.orig_b_time = int(burst_time)
		self.orig_iotime = int(io_time)
		self.prio = int(priority)
		self.age_time = int(burst_time)*3
		self.wait_time = 13
	def __cmp__(self,other):
		return cmp(self.b_time,other.b_time)

class cpu_process_by_p(cpu_process):
	def __init__(self,proc_num,burst_time,num_bursts,io_time,priority):
		super(cpu_process_by_p,self).__init__(proc_num,burst_time,num_bursts,io_time,priority)
	def __cmp__(self,other):
		return cmp(self.b_time,other.b_time)

def print_queue(queue):
	if len(queue) == 0:
		return "]"
	x = 0;
	rets = ' '
	while x < len(queue):
		if x < len(queue) - 1:
			rets += str(queue[x].name)+' '
		else:
			rets += str(queue[x].name)
		x+=1
	rets += "]"
	return rets


def run_processes_fcfs(proc_lis):
	queue = []
	for proc in proc_lis:
		queue.append(proc)
	n = len(queue)
	t_cs = 0
	print "time", str(t_cs) + "ms: Simulator started for FCFS [Q"+print_queue(queue)
	run_slot = []
	io_set = []
	while len(queue) > 0 or len(run_slot) > 0 or len(io_set) > 0:
		t_cs += 1
		if len(run_slot) == 0 and len(queue) > 0:
			queue[0].wait_time -= 1
			if queue[0].wait_time == 0:
				queue[0].wait_time = 13
				run_slot.append(queue.pop(0))
				print "time", str(t_cs) + "ms: P" + str(run_slot[0].name) + " started using the CPU [Q"+print_queue(queue)
		if len(run_slot) == 1:
			if run_slot[0].b_time == 0:
				run_slot[0].b_time = run_slot[0].orig_b_time
				run_slot[0].num_b -= 1
				if run_slot[0].num_b == 0:
					print "time", str(t_cs) + "ms: P" + str(run_slot[0].name) + " terminated [Q"+print_queue(queue)
					run_slot.pop(0)
				else:
					print "time", str(t_cs) + "ms: P" + str(run_slot[0].name) + " completed its CPU burst [Q"+print_queue(queue)
					print "time", str(t_cs) + "ms: P" + str(run_slot[0].name) + " performing I/O [Q"+print_queue(queue)
					io_set.append(run_slot.pop(0))
					io_set.sort(key=operator.attrgetter('name'))
			else:
				run_slot[0].b_time -= 1
		if len(io_set) != 0:
			z = 0
			while z < len(io_set):
				if io_set[z].iotime == 0:
					io_set[z].iotime = io_set[z].orig_iotime
					queue.append(io_set.pop(z))
					print "time", str(t_cs) + "ms: P" + str(queue[-1].name) + " completed I/O [Q"+print_queue(queue)
				else:
					io_set[z].iotime -= 1
					z += 1
	print "time", str(t_cs) + "ms: Simulator ended"

if __name__ == "__main__":
	fil = open('processes.txt','r')
	#print fil
	read_file = fil.read()
	words = read_file.split("\n")
	x = 0
	while x < len(words):
		#print words[x]
		if words[x][0] == '#':
			words.remove(words[x]);
		else:
			x+=1
	proc_lis = []
	for line in words:
		final = line.split('|')
		proc_lis.append(cpu_process(final[0],final[1],final[2],final[3],final[4]))
	run_processes_fcfs(proc_lis)

	#print read_file
