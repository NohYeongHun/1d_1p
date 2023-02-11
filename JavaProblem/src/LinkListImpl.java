public class LinkListImpl {

    public static void main(String[] args) {
        LinkList linkList = new LinkList(new Node(0, null, null));
        linkList.add(new Node(1, null, null));
        System.out.println(linkList.search(1));
    }
    
}

class Node{
    int data;
    Node prev;
    Node next;

    Node(int data, Node prev, Node next){
        this.data = data;
        this.prev = prev;
        this.next = next;
    }
}

class LinkList {
    Node head;

    LinkList(Node node){
        this.head = node;
    }

    void add(Node addNode){
        Node node = head;

        // node 이동
        while(node.next != null){
            node = node.next;
        }
        node.next = addNode;
        addNode.prev = node;
    }

    void remove(int data){
        Node node = head;

        while(node.data != data){
            node = node.next;
        }
        Node prevNode = node.prev;
        Node nextNode = node.next;

        prevNode.next = node.next;
        nextNode.prev = node.prev;
    }

    int search(int data){
        Node node = head;
        int idx = 0;

        while(node.data != data){
            node = node.next;
            idx += 1;
        }

        return idx;

    }
}
