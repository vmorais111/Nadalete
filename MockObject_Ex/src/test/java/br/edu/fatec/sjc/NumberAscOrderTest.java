package br.edu.fatec.sjc;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.Mockito;
import org.mockito.junit.jupiter.MockitoExtension;

@ExtendWith(MockitoExtension.class)
public class NumberAscOrderTest {

    @Mock
    CalculableStrategy<Double> calculableStrategy;

    private CustomStack<Double> stack;

    @BeforeEach
    public void setup() {
        stack = new CustomStack<>(6, calculableStrategy);
    }

    @Test
    public void testSortWithSixRandomNumbers() throws StackFullException, StackEmptyException {
        Mockito.when(calculableStrategy.calculateValue(Mockito.anyDouble()))
                .thenAnswer(invocation -> invocation.getArgument(0));

        stack.push(42.0);
        stack.push(7.0);
        stack.push(13.0);
        stack.push(29.0);
        stack.push(5.0);
        stack.push(60.0);

        NumberAscOrder<Double> sorter = new NumberAscOrder<>(stack);
        List<Double> sorted = sorter.sort();

        assertEquals(6, sorted.size());
        assertEquals(List.of(5.0, 7.0, 13.0, 29.0, 42.0, 60.0), sorted);
    }

    @Test
    public void testSortWithEmptyStack() throws StackEmptyException {
        NumberAscOrder<Double> sorter = new NumberAscOrder<>(stack);
        List<Double> sorted = sorter.sort();

        assertTrue(sorted.isEmpty());
    }
}
