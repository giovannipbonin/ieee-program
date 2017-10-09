
## Trees
Trees are again just another form of organizing data in a way that provides benefits for certain applications. It is called a Tree because it has branches, like real life trees do. Most think of it as an upside down tree. 
In general:
```
class Node {
    public String name;
    public Node[] children;
}

class Tree {
    public Node root;
}
```

### Balanced vs. Unbalanced Trees

### Complete Binary Tree

### Perfect Binary Tree


## Binary Search Trees
    - Trees come in all sorts and forms, depending on the application we are desigining them for there are advantages in choosing one type from another, and we will look at each of those indidually as well as examine the trade-offs in future sessions. But it is easy to understand the great advantage of trees at all by talking about binary search trees (BSTs). Their one rule is that:
    - For every node, its left child contains a value smaller than or equal to itself, and its right child is larger. E.g:
    4
   / \
  2   5
 / \
1   3

```
class Node {
    public String name;
    public Node left;
    public Node right;
}
```

We can see that finding an element here only takes O(log(n)) time for a generally balanced tree. We will also looking at the problem of unbalenced trees later (where most the height of one of the children is much larger than the other, and worst case run time is O(n), to solve this we have balancing algorithms)

Videos:
- [ ] [Series: Core Trees (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/ovovP/core-trees)
- [ ] [Series: Trees (video)](https://www.coursera.org/learn/data-structures/lecture/95qda/trees)
- [ ] [Series (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/p82sw/core-introduction-to-binary-search-trees)


### Tree Traversals
1. `In-Order`
    1. `In-Order` on left branch
    2. Get current `Node`'s value
    3. `In-Order` on right branch
2. Pre-Order
    1. You tell me
3. Post-Order
    1. Josh? Brandon? Melanie?
    
  
## Heaps

- ### Tries
     - https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/08Xyf/core-introduction-to-tries
     - https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/PvlZW/core-performance-of-tries
     - https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/DFvd3/core-implementing-a-trie


    
### Graphs
   - Graphs, just like trees, are another way to represent data. A tree is actually just a specific form of a graph. Graphs are very important when we want to model items that have a relationship with one another, like trees. Every tree is a graph, but not every graph is a tree because some graphs can contain cycles (loops) and trees cannot. 
 
 Videos: 
 - [BFS](https://www.youtube.com/watch?v=QRq6p9s8NVg)
 - [DFS](https://www.youtube.com/watch?v=QRq6p9s8NVg)
 - [Graph representation](https://www.youtube.com/watch?v=WQ2Tzlxl_Xo)
 
 
### Home reading:
- [MIT (video)](https://www.youtube.com/watch?v=s-CYnVz-uh4&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=13)
- [Priority Queues] (https://www.youtube.com/watch?v=-WEku8ZnynU)
 - [ ] [CSE373 2012 - Lecture 11 - Graph Data Structures (video)](https://www.youtube.com/watch?v=OiXxhDrFruw&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b&index=11)
 - [ ] [CSE373 2012 - Lecture 12 - Breadth-First Search (video)](https://www.youtube.com/watch?v=g5vF8jscteo&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b&index=12)





## Session 1 - Search Trees,  and Balanced Trees

For interviews, definitely know the properties and implementation of binary search trees. For balanced trees, know the general advantages of each, but you will probably not be asked to straight up implement an AVL Tree. You might have to do something that uses that idea where you would more or less end up inventing it on the fly.

- ### Binary search trees: BSTs
    - [ ] [Series](https://www.coursera.org/learn/data-structures/lecture/E7cXP/introduction)

- ### Balanced search trees
 - AVL trees
          - https://www.coursera.org/learn/data-structures/lecture/Qq5E0/avl-trees
          - https://www.coursera.org/learn/data-structures/lecture/PKEBC/avl-tree-implementation
          - https://www.coursera.org/learn/data-structures/lecture/22BgE/split-and-merge
          
 - 2-3 search trees
     - https://www.coursera.org/learn/algorithms-part1/lecture/wIUNW/2-3-search-trees
 - Red-black trees
     - https://www.coursera.org/learn/algorithms-part1/lecture/GZe13/red-black-bsts
 - B-trees
     - https://www.coursera.org/learn/algorithms-part1/lecture/HIlHd/b-trees-optional
    


### Home Reading:

- **Splay trees**
        - In practice:
            Splay trees are typically used in the implementation of caches, memory allocators, routers, garbage collectors,
            data compression, ropes (replacement of string used for long text strings), in Windows NT (in the virtual memory,
            networking, and file system code) etc.
        - [ ] [CS 61B: Splay Trees (video)](https://www.youtube.com/watch?v=Najzh1rYQTo&index=23&list=PL-XXv-cvA_iAlnI-BQr9hjqADPBtujFJd
        
- [ ] MIT Lecture: Splay Trees:
            - Gets very mathy, but watch the last 10 minutes for sure.
            - [Video](https://www.youtube.com/watch?v=QnPl_Y6EqMo)
  - 2-3 Trees:          
    - [ ] [23-Tree Intuition and Definition (video)](https://www.youtube.com/watch?v=C3SsdUqasD4&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6&index=2)
        - [ ] [Binary View of 23-Tree](https://www.youtube.com/watch?v=iYvBtGKsqSg&index=3&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6)
        - [ ] [2-3 Trees (student recitation) (video)](https://www.youtube.com/watch?v=TOb1tuEZ2X4&index=5&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp)

 -  **Red/black trees**
        - In practice:
            Red–black trees offer worst-case guarantees for insertion time, deletion time, and search time.
            Not only does this make them valuable in time-sensitive applications such as real-time applications,
            but it makes them valuable building blocks in other data structures which provide worst-case guarantees;
            for example, many data structures used in computational geometry can be based on red–black trees, and
            the Completely Fair Scheduler used in current Linux kernels uses red–black trees. In the version 8 of Java,
            the Collection HashMap has been modified such that instead of using a LinkedList to store identical elements with poor
            hashcodes, a Red-Black tree is used.
        - [ ] [Aduni - Algorithms - Lecture 4 (link jumps to starting point) (video)](https://youtu.be/1W3x0f_RmUo?list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&t=3871)
        - [ ] [Aduni - Algorithms - Lecture 5 (video)](https://www.youtube.com/watch?v=hm2GHwyKF1o&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=5)
        - [ ] [Black Tree](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree)
        - [ ] [An Introduction To Binary Search And Red Black Tree](https://www.topcoder.com/community/data-science/data-science-tutorials/an-introduction-to-binary-search-and-red-black-trees/)
        - https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/8acpe/red-black-trees
        - https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/JV7KI/rotations-advanced-optional
        - https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/jPL2x/insertion-in-a-red-black-tree-advanced

 
- **2-3-4 Trees (aka 2-4 trees)**
        - In practice:
            For every 2-4 tree, there are corresponding red–black trees with data elements in the same order. The insertion and deletion
            operations on 2-4 trees are also equivalent to color-flipping and rotations in red–black trees. This makes 2-4 trees an
            important tool for understanding the logic behind red–black trees, and this is why many introductory algorithm texts introduce
            2-4 trees just before red–black trees, even though **2-4 trees are not often used in practice**.
        - [ ] [CS 61B Lecture 26: Balanced Search Trees (video)](https://www.youtube.com/watch?v=zqrqYXkth6Q&index=26&list=PL4BBB74C7D2A1049C)
        - [ ] [Bottom Up 234-Trees (video)](https://www.youtube.com/watch?v=DQdMYevEyE4&index=4&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6)
        - [ ] [Top Down 234-Trees (video)](https://www.youtube.com/watch?v=2679VQ26Fp4&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6&index=5)

-  **B-Trees**
        - fun fact: it's a mystery, but the B could stand for Boeing, Balanced, or Bayer (co-inventor)
        - In Practice:
            B-Trees are widely used in databases. Most modern filesystems use B-trees (or Variants). In addition to
            its use in databases, the B-tree is also used in filesystems to allow quick random access to an arbitrary
            block in a particular file. The basic problem is turning the file block i address into a disk block
            (or perhaps to a cylinder-head-sector) address.
        - [ ] [B-Tree](https://en.wikipedia.org/wiki/B-tree)
        - [ ] [Introduction to B-Trees (video)](https://www.youtube.com/watch?v=I22wEC1tTGo&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6&index=6)
        - [ ] [B-Tree Definition and Insertion (video)](https://www.youtube.com/watch?v=s3bCdZGrgpA&index=7&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6)
        - [ ] [B-Tree Deletion (video)](https://www.youtube.com/watch?v=svfnVhJOfMc&index=8&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6)
        - [ ] [MIT 6.851 - Memory Hierarchy Models (video)](https://www.youtube.com/watch?v=V3omVLzI0WE&index=7&list=PLUl4u3cNGP61hsJNdULdudlRL493b-XZf)
                - covers cache-oblivious B-Trees, very interesting data structures
                - the first 37 minutes are very technical, may be skipped (B is block size, cache line size)


- ### N-ary (K-ary, M-ary) trees
    - note: the N or K is the branching factor (max branches)
        - binary trees are a 2-ary tree, with branching factor = 2
        - 2-3 trees are 3-ary
    - [ ] [K-Ary Tree](https://en.wikipedia.org/wiki/K-ary_tree)
 


    
  



### Home Reading
   - [ ] [MIT (video)](https://www.youtube.com/watch?v=9Jry5-82I68)
      - [ ] [Sedgewick - Tries (3 videos)](https://www.youtube.com/playlist?list=PLe-ggMe31CTe9IyG9MB8vt5xUJeYgOYRQ)
        - [ ] [1. R Way Tries](https://www.youtube.com/watch?v=buq2bn8x3Vo&index=3&list=PLe-ggMe31CTe9IyG9MB8vt5xUJeYgOYRQ)
        - [ ] [2. Ternary Search Tries](https://www.youtube.com/watch?v=LelV-kkYMIg&index=2&list=PLe-ggMe31CTe9IyG9MB8vt5xUJeYgOYRQ)
        - [ ] [3. Character Based Operations](https://www.youtube.com/watch?v=00YaFPcC65g&list=PLe-ggMe31CTe9IyG9MB8vt5xUJeYgOYRQ&index=1)
    - [ ] [Notes on Data Structures and Programming Techniques](http://www.cs.yale.edu/homes/aspnes/classes/223/notes.html#Tries)
    - [ ] Short course videos:
        - [ ] [Introduction To Tries (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/08Xyf/core-introduction-to-tries)
        - [ ] [Performance Of Tries (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/PvlZW/core-performance-of-tries)
        - [ ] [Implementing A Trie (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/DFvd3/core-implementing-a-trie)
    - [ ] [The Trie: A Neglected Data Structure](https://www.toptal.com/java/the-trie-a-neglected-data-structure)
    - [ ] [TopCoder - Using Tries](https://www.topcoder.com/community/data-science/data-science-tutorials/using-tries/)
    - [ ] [Stanford Lecture (real world use case) (video)](https://www.youtube.com/watch?v=TJ8SkcUSdbU)
    - [ ] [Series (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/p82sw/core-introduction-to-binary-search-trees)

- ### Heap / Priority Queue / Binary Heap
    - visualized as a tree, but is usually linear in storage (array, linked list)
    - [ ] [Heap](https://en.wikipedia.org/wiki/Heap_(data_structure))
    - https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/iIzo8/heaps-operations-and-applications
    - https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/KKqlm/heaps-implementation-details-advanced-optional
    - [ ] [Naive Implementations (video)](https://www.coursera.org/learn/data-structures/lecture/z3l9N/naive-implementations)
    - [ ] [Binary Trees (video)](https://www.coursera.org/learn/data-structures/lecture/GRV2q/binary-trees)
    - [ ] [Basic Operations (video)](https://www.coursera.org/learn/data-structures/lecture/0g1dl/basic-operations)
    - [ ] [Complete Binary Trees (video)](https://www.coursera.org/learn/data-structures/lecture/gl5Ni/complete-binary-trees)
    - [ ] [Pseudocode (video)](https://www.coursera.org/learn/data-structures/lecture/HxQo9/pseudocode)
    - [ ] [Heap Sort - jumps to start (video)](https://youtu.be/odNJmw5TOEE?list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&t=3291)
    - [ ] [Heap Sort (video)](https://www.coursera.org/learn/data-structures/lecture/hSzMO/heap-sort)
    - [ ] [Building a heap (video)](https://www.coursera.org/learn/data-structures/lecture/dwrOS/building-a-heap)
    - [ ] [CS 61B Lecture 24: Priority Queues (video)](https://www.youtube.com/watch?v=yIUFT6AKBGE&index=24&list=PL4BBB74C7D2A1049C)
    - [ ] [Linear Time BuildHeap (max-heap)](https://www.youtube.com/watch?v=MiyLo8adrWw)
    - [ ] Implement a max-heap:
        - [ ] insert
        - [ ] sift_up - needed for insert
        - [ ] get_max - returns the max item, without removing it
        - [ ] get_size() - return number of elements stored
        - [ ] is_empty() - returns true if heap contains no elements
        - [ ] extract_max - returns the max item, removing it
        - [ ] sift_down - needed for extract_max
        - [ ] remove(i) - removes item at index x
        - [ ] heapify - create a heap from an array of elements, needed for heap_sort
        - [ ] heap_sort() - take an unsorted array and turn it into a sorted array in-place using a max heap
            - note: using a min heap instead would save operations, but double the space needed (cannot do in-place).
            
            

- ### Treap
    - Combination of a binary search tree and a heap
    - [ ] [Treap](https://en.wikipedia.org/wiki/Treap)
    - [ ] [Data Structures: Treaps explained (video)](https://www.youtube.com/watch?v=6podLUYinH8)
    - [ ] [Applications in set operations](https://www.cs.cmu.edu/~scandal/papers/treaps-spaa98.pdf)
        

# Week 6


## Session 1 - Graph Properties and Graph Search


- https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/NX0BI/graph-search-overview till 6:50
- https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/JZRXz/breadth-first-search-bfs-the-basics
- https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/ZAaJA/bfs-and-shortest-paths <-
- https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/BTVWn/bfs-and-undirected-connectivity
- https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/pKr0Y/depth-first-search-dfs-the-basics


Dijkstra Graph Search Algorihtm
- https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/rxrPa/dijkstras-shortest-path-algorithm till 10:00
- https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/Jfvmn/dijkstras-algorithm-examples

### Home Reading
- https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/VCHYw/correctness-of-dijkstras-algorithm
- https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/Pbpp9/dijkstras-algorithm-implementation-and-running-time
- https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/yeKm7/topological-sort till 10:00
- https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/rng2S/computing-strong-components-the-algorithm
- https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/f11at/structure-of-the-web-optional



### Session 2 - Solving Problems Using Graphs

Use this: https://www.coursera.org/learn/algorithms-on-graphs

### Home Reading

Graphs are a huge subject in computer science, there are many applications in which they are powerful. From modeling the relationships between people in social networks, to representing connections of genomic data in trying to understand patterns of diseases, they are very useful. There are many ways to represent them and we will understand them below: 


- [ ] **Union-Find**
    - [ ] [Overview](https://www.coursera.org/learn/data-structures/lecture/JssSY/overview)
    - [ ] [Naive Implementation](https://www.coursera.org/learn/data-structures/lecture/EM5D0/naive-implementations)
    - [ ] [Trees](https://www.coursera.org/learn/data-structures/lecture/Mxu0w/trees)
    - [ ] [Union By Rank](https://www.coursera.org/learn/data-structures/lecture/qb4c2/union-by-rank)
    - [ ] [Path Compression](https://www.coursera.org/learn/data-structures/lecture/Q9CVI/path-compression)
    - [ ] [Analysis Options](https://www.coursera.org/learn/data-structures/lecture/GQQLN/analysis-optional)
    - [ ] [Sedgewick Algorithms - Union-Find (6 videos)](https://www.youtube.com/watch?v=8mYfZeHtdNc&list=PLe-ggMe31CTexoNYnMhbHaWhQ0dvcy43t)


- [ ] **Advanced Graph Processing** (videos)
    - [ ] [Synchronous Distributed Algorithms: Symmetry-Breaking. Shortest-Paths Spanning Trees](https://www.youtube.com/watch?v=mUBmcbbJNf4&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=27)
    - [ ] [Asynchronous Distributed Algorithms: Shortest-Paths Spanning Trees](https://www.youtube.com/watch?v=kQ-UQAzcnzA&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=28)



- use resources from here https://www.coursera.org/learn/algorithms-on-graphs 
- https://www.coursera.org/learn/algorithms-graphs-data-structures
 

