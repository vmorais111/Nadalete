package br.edu.fatec.sjc;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class NumberAscOrder<T extends Number> {

    private final CustomStack<T> stack;

    public NumberAscOrder(CustomStack<T> stack) {
        this.stack = stack;
    }

    public List<T> sort() throws StackEmptyException {
        if (stack == null || stack.isEmpty()) {
            return new ArrayList<>();
        }

        List<T> result = new ArrayList<>();

        while (!stack.isEmpty()) {
            result.add(stack.pop());
        }

        Collections.sort(result, (a, b) -> Double.compare(a.doubleValue(), b.doubleValue()));

        return result;
    }
}
