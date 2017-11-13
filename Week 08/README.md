# Operating Systems

## Concepts to touch upon
1. Multi-processing vs. Multi-Threading
2. I/O-Bound vs. CPU-Bound Tasks

## Processes
1. Loads a program into memory.
2. Executes the program.
3. Handles program's execution.
4. Provides a mechanism for process synchronization.
5. Provides a mechanism for process communication.
6. Provides a mechanism for deadlock handling.

### Process States
1. Start
2. Ready
3. Running
4. Waiting
5. Terminated

### Parts of a Process 
1. **Stack** - method parameters, return addresses, and local variables
2. **Heap** - Dynamically allocated memory
3. **Data** - Static and global variables

## Process Scheduling
1. Program needs to read a file or write a file.
2. The operating system gives the permission to the program for operation on file.
3. Permission varies from read-only, read-write, denied and so on.
4. Operating System provides an interface to the user to create/delete files.
5. Operating System provides an interface to the user to create/delete directories.
![alt-text](https://www.tutorialspoint.com/operating_system/images/queuing_diagram.jpg)

### Context Switching
![alt-text](https://www.tutorialspoint.com/operating_system/images/context_switch.jpg)

### Hyper-Threading
```
Hyper-threading is where your processor pretends to have 2 physical processor cores, yet only has 1 and some extra junk.

The point of hyperthreading is that many times when you are executing code in the processor, there are parts of the processor that is idle. By including an extra set of CPU registers, the processor can act like it has two cores and thus use all parts of the processor in parallel. When the 2 cores both need to use one component of the processor, then one core ends up waiting of course. This is why it can not replace dual-core and such processors.
```

## Multi-Threading
![alt-text](https://www.tutorialspoint.com/operating_system/images/thread_processes.jpg)

## Scheduling algorithms
## Memory management
[User vs. Kernel Mode](https://blog.codinghorror.com/understanding-user-and-kernel-mode/)

## Virtual memory
## Drivers
## File System

# Concurrency
[Intro to Concurrency](http://cs.lmu.edu/~ray/notes/introconcurrency/)

## Scheduling
1. Need to be aware of how your operating system and programming language deal with concurrency
## Communication
1. Shared memory
2. Message passing

## Concurrency Models
1. Mutex
2. Semaphore

## Correctness
Concurrent programs have to be correct for all possible interleavings. Naturally this makes testing more complicated, but it can be done.




Very Basics first: 

- [ ] [How does CPU execute program (video)](https://www.youtube.com/watch?v=42KTvGYQYnA)
- [ ] [Machine Code Instructions (video)](https://www.youtube.com/watch?v=Mv2XQgpbTNE)
- [ ] [threads in C++ (series - 10 videos)](https://www.youtube.com/playlist?list=PL5jc9xFGsL8E12so1wlMS0r0hTQoJL74M)
- [ ] concurrency in Python (videos):
- [ ] [Short series on threads](https://www.youtube.com/playlist?list=PL1H1sBF1VAKVMONJWJkmUh6_p8g4F2oy1)
- [ ] [Python Threads](https://www.youtube.com/watch?v=Bs7vPNbB9JM)
- [ ] [Mutex in Python](https://www.youtube.com/watch?v=0zaPs8OtyKY)

### Home Reading
- [Operating Systems and System Programming (video)](https://www.youtube.com/playlist?list=PL-XXv-cvA_iBDyz-ba4yDskqMDY6A1w_c)
- [What Is The Difference Between A Process And A Thread?](https://www.quora.com/What-is-the-difference-between-a-process-and-a-thread
-  [Count Bits](https://graphics.stanford.edu/~seander/bithacks.html#CountBitsSetKernighan)
 [Bit Manipulation (video)](https://www.youtube.com/watch?v=7jkIUgLC29I)
- ### Computer Security
    - [MIT (23 videos)](https://www.youtube.com/playlist?list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh)
        - [ ] [Introduction, Threat Models](https://www.youtube.com/watch?v=GqmQg-cszw4&index=1&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh)
        - [ ] [Control Hijacking Attacks](https://www.youtube.com/watch?v=6bwzNg5qQ0o&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh&index=2)
        - [ ] [Buffer Overflow Exploits and Defenses](https://www.youtube.com/watch?v=drQyrzRoRiA&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh&index=3)
        - [ ] [Privilege Separation](https://www.youtube.com/watch?v=6SIJmoE9L9g&index=4&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh)
        - [ ] [Capabilities](https://www.youtube.com/watch?v=8VqTSY-11F4&index=5&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh)
        - [ ] [Sandboxing Native Code](https://www.youtube.com/watch?v=VEV74hwASeU&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh&index=6)
        - [ ] [Web Security Model](https://www.youtube.com/watch?v=chkFBigodIw&index=7&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh)
        - [ ] [Securing Web Applications](https://www.youtube.com/watch?v=EBQIGy1ROLY&index=8&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh)
        - [ ] [Symbolic Execution](https://www.youtube.com/watch?v=yRVZPvHYHzw&index=9&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh)
        - [ ] [Network Security](https://www.youtube.com/watch?v=SIEVvk3NVuk&index=11&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh)
        - [ ] [Network Protocols](https://www.youtube.com/watch?v=QOtA76ga_fY&index=12&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh)
        - [ ] [Side-Channel Attacks](https://www.youtube.com/watch?v=PuVMkSEcPiI&index=15&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh)
