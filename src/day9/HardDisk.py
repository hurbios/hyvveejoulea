class HardDisk:
    def __init__(self, files):
        self._files = files # []
        self._defragmented = []
        self._fragmented = []
        self._get_defragmented()

    def _get_defragmented(self):
        for i, file in enumerate(self._files):
            for _ in range(int(file)):
                self._defragmented.append(i//2 if i % 2 == 0 else ".")

    def get_defragmented_disk(self):
        return self._defragmented

    def get_fragmented_disk(self):
        return self._fragmented

    def fragment_disk(self):
        empty_blocks = 0
        self.original_length = len(self._defragmented)
        for block in self._defragmented:
            if block == ".":
                empty_blocks+=1
                popped = None
                while not popped and len(self._fragmented) + empty_blocks <= self.original_length:
                    popped = self._defragmented.pop()
                    if popped == ".":
                        popped = None
                        empty_blocks += 1
                if popped:
                    self._fragmented.append(popped)
            else:
                self._fragmented.append(block)
        self._empty_block = empty_blocks

    def get_checksum(self):
        checksum = 0
        for i, block in enumerate(self._fragmented):
            checksum += i * int(block)
        return checksum

    def get_sizes(self):
        return (self._empty_block, len(self._fragmented), self.original_length)
