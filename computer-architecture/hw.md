### 1.
2. fetch, decode and execute
3. ALU or the arithmetic logic unit is responsible for arithmetic operations, such as addition and substraction, as well as logical operations like AND.
4. The program counter updates on each fetch cycle providing the next memory address to fetch an instruction from.
5. When fetching data or an instruction from a specific memory address, the address bus is first used to locate the specified memory address. Then the data bus is used to transmit the contents of that memory address to the CPU. When changing the contents of a memory address, the address is first opened using the address bus, after which the new data is transmitted from the CPU using the data bus.
6. External storage is a great way to store data that often needs to be accessed on two or more computers that aren't always on the same network.
7. Cache memory is beneficial, because it ensures that more fundamental operations and data are accessible by the CPU as fast as possible. It provides more layers to storing data, with each one being slower but larger in size. This allows for more specialized storage for data with different levels of importance.

### 2. 
2. Pipelining overlaps the execution of multiple instructions, reducing the time it takes to execute the set of instructions for multiple data sets. This makes a program much faster.
3. A GPU is faster than a CPU when it needs to process large amounts of data. A GPU also has a large number of cores, which makes it ideal for doing similar calculations in parallel.
4. A CPU has has only a few cores compared to a GPU, but CPU cores are much more powerful. Because of this, a CPU can handle more complex single tasks, while a GPU is best suited for handling the same task multiple times in parallel due to it's high core count.
5. 
    1. The CPU transmits unprocessed data to the GPU via the data bus
    2. The GPU loads the unprocessed data to VRAM and processes it in parallel
    3. The CPU copies the result from VRAM to RAM via the data bus
