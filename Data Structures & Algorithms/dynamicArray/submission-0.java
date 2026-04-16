class DynamicArray {
    private int[] array;
    public int capacity;
    public int currSize;
    public DynamicArray(int capacity) {
        this.capacity = capacity;
        this.currSize = 0;
        this.array = new int[capacity];
    }

    public int get(int i) {
        return array[i];
    }

    public void set(int i, int n) {
        array[i] = n;
    }

    public void pushback(int n) {
        if (currSize == capacity) {
            resize();
        }
        array[currSize] = n;
        currSize++;
    }

    public int popback() {
        if (currSize>0) {
            currSize--;
            return array[currSize];
        }
        return -1;
    }

    private void resize() {
        capacity = capacity*2;
        int[] newArray = new int[capacity];
        for (int i=0; i< currSize; i++) {
            newArray[i] = array[i];
        }
        array = newArray;
    }

    public int getSize() {
        return this.currSize;
    }

    public int getCapacity() {
        return this.capacity;
    }
}
