class HardDisk:
    def __init__(self, files):
        self._files = files # []
        self._defragmented = []
        self._fragmented = []
        self._get_defragmented()
        self._file_segments = []

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
    
    def reset_defracmented(self):
        self._defragmented = []
        self._get_defragmented()

    # changes file blocks to reflect changes, moves files in defragmented.
    def _move_file_block(self, empty_block, movable_block):
        starting_point = self._file_segments[empty_block][0]
        ending_point = self._file_segments[empty_block][0]+self._file_segments[movable_block][1]-self._file_segments[movable_block][0]

        for i in range(starting_point,ending_point): # todo verify: does this replace the block contents
            self._defragmented[i] = self._file_segments[movable_block][2]
        for i in range(self._file_segments[movable_block][0], self._file_segments[movable_block][1]): # todo: change from the end as well
            self._defragmented[i] = "."
        
        self._file_segments[empty_block]=(ending_point, self._file_segments[empty_block][1], self._file_segments[empty_block][2], self._file_segments[empty_block][3]) # shorten empty block
        self._file_segments[empty_block-1]=(self._file_segments[empty_block-1][0], self._file_segments[empty_block-1][1], self._file_segments[empty_block-1][2], self._file_segments[empty_block-1][3] + self._file_segments[movable_block][1]-self._file_segments[movable_block][0]) # increase previous block

    def file_move(self):
        pointer = 0
        for i,file in enumerate(self._files):
            self._file_segments.append((pointer, pointer + int(file), i//2 if i%2 == 0 else ".",0)) # (start, end, ID, grown)
            pointer += int(file)
        #print(self._file_segments)
        #reversed_segments = self._file_segments.copy()
        #reversed_segments.reverse()
        segment_len = len(self._file_segments)
        for i in range((segment_len - segment_len % 2), 0, -2): # go through files to move
            #print(i)
            #current_filled_block_index = 2 * i + len(reversed_segments) % 2
            # print(current_filled_block_index)
            for y in range(1,i,2): # go through empty spaces to move to
                empty_len = self._file_segments[y][1] - self._file_segments[y][0] + self._file_segments[y][3]
                movable_len = self._file_segments[i][1] - self._file_segments[i][0] #+ self._file_segments[i][3]
                #print(f"empty len {y}: {empty_len}, movable len {i}: {movable_len}")
                if empty_len >= movable_len:
                    self._move_file_block(y, i)
                    #print("test")
                    break            
        #print(self._file_segments)
            

    def get_checksum(self):
        checksum = 0
        for i, block in enumerate(self._fragmented):
            checksum += i * int(block)
        return checksum
    
    def get_defragmented_checksum(self):
        checksum = 0
        for i, block in enumerate(self._defragmented):
            if block != ".":
                checksum += i * int(block)
        return checksum

    def get_sizes(self):
        return (self._empty_block, len(self._fragmented), self.original_length)

