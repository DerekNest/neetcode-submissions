class Node {
        int val;
        Node next;
        public Node(int val) {
            this.val = val;
            this.next = null;
        }
    }
class LinkedList {
    private Node head;
    private Node tail;

    public LinkedList() {
        this.head = new Node(-1);
        this.tail = this.head;
    }

    public int get(int index) {
        Node curr = head.next;
        int i =0;
        while (curr!= null && i< index) {
            curr = curr.next;
            i++;
        }
        return (curr!= null) ? curr.val :-1;
        
    }

    public void insertHead(int val) {
        Node newNode = new Node(val);
        newNode.next = head.next;
        head.next = newNode;
        if (newNode.next == null) {
            tail=newNode;
        }
    }

    public void insertTail(int val) {
        Node newNode = new Node(val);
        tail.next = newNode;
        tail = newNode;
    }

    public boolean remove(int index) {
        Node curr = head;
        int i = 0;
        while (i < index && curr.next !=null) {
            curr = curr.next;
            i++;
        }
        if (curr!= null && curr.next != null) {
            if (curr.next == tail) {
                tail = curr;
            }
            curr.next = curr.next.next;
            return true;
        }
        return false;
    }

    public ArrayList<Integer> getValues() {
        ArrayList<Integer> values = new ArrayList<>();
        Node curr = head.next;
        while(curr !=null){
            values.add(curr.val);
            curr=curr.next;
        }
        return values;
    }
}
