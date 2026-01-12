The intel 4004 by todays standards is exceptionally simple, which could also be a testament to it's genius. The architecture was not the hard part of the design but it is what we are covering in this document.

The chip connects to the outside world through 16 gold plated pins. A 4 bit internal data bus is the main nerve of the cpu. from there we fan out to the accumulator, temp register, and flag flip-flops.

These blocks feed the 4 bit ALU capable of binary and decimal arithmatic(no floating point operations). The ALU feeds it's data back onto the data bus.

The 4004 features a 3 layer stack, and 16 I/O registers 4 bits each accessable through a Register multiplexer.

The 4004 is directly compatible with the 4001(ROM), 4002(RAM), and 4003(Shift Register)

Power is procided by two rails -10, and +5.

We will cover this more in the historical digest of the 4004's development but the 4004 was made possible through the development of silicon gates. This allowed faster switching of transistors and improved power. Can you guess who developed this technology?(Hint: He was pretty instrumental to the 4004)

The clock is unique for the period having two phases.

Below is the block diagram of the 4004 and the pin out of the DIP package!

![4004 Block Diagram](docs/architecture/block-diagrams/4004-block-diagram.webp)
![4004 Pinout](docs/architecture/block-diagrams/4004-pinout.jpg)

