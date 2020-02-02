public class MergeX implements Comparable<Merge> {
    private static Comparable[] aux;

    private static boolean less(Comparable v, Comparable w) {
        return v.compareTo(w) < 0;
    }

    @Override
    public int compareTo(Merge arg0) {
        // TODO Auto-generated method stub
        return 0;
    }

    public static void merge(Comparable[] a, Comparable[] aux, int lo, int mid, int hi) {
        int i = lo, j = mid + 1;
        // for (int k = lo; k <= hi; k++) {
        // aux[k] = a[k];
        // }
        for (int k = lo; k <= hi; k++) {
            if (i > mid) {
                a[k] = aux[j++];
            } else if (j > hi) {
                a[k] = aux[i++];
            } else if (less(aux[j], aux[i])) {
                a[k] = aux[j++];
            } else {
                a[k] = aux[i++];
            }
        }
    }

    public static void sort(Comparable[] a) {
        aux = a.clone();
        sort(a, aux, 0, a.length - 1);
    }

    private static void sort(Comparable[] a, Comparable[] aux, int lo, int hi) {

        int mid = lo + (hi - lo) / 2;
        if (hi - lo <= 7) {
            insertionSort(a, lo, hi);
            return;
        }
        sort(aux, a, lo, mid);
        sort(aux, a, mid + 1, hi);
        if (!less(aux[mid + 1], aux[mid])) {
            System.arraycopy(aux, lo, a, lo, hi-lo+1);
            return;
        }
        merge(a, aux, lo, mid, hi);
    }

    private static void insertionSort(Comparable[] a, int lo, int hi) {
        for (int i = lo; i <= hi; i++)
            for (int j = i; j > lo && less(a[j], a[j - 1]); j--)
                exch(a, j, j - 1);
    }

    private static void exch(Comparable[] a, int j, int i) {
        Comparable temp;
        temp = a[j];
        a[j] = a[i];
        a[i] = temp;
    }

    public static void main(String[] args) {
        MergeX mgx = new MergeX();
        Comparable a[] = { 8, 1, 6, 8, 4, 6, 9,7,1, 2, 3,4,8,5,2,6,4,3,8};
        mgx.sort(a);
        for (int i = 0; i < a.length; i++) {
            System.out.print(a[i] + " ");
        }
    }
}