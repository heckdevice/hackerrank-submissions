package heckdevice.hackerrank.samples;

import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Scanner;

/**
 * Created by heckdevice on 13/09/14.
 */
public class GemStone {

    static boolean printInfo = false;
    static char[] elementsType = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};

    public static void main(String[] args) {
        Scanner readStdIn = new Scanner(System.in);

        int numberOfRocks = readStdIn.nextInt();
        String[] elements = new String[numberOfRocks];
        for (int count = 0; count < numberOfRocks; count++) {
            elements[count] = readStdIn.next();
        }
        if (printInfo)
            for (int count = 0; count < numberOfRocks; count++)
                System.out.println("Number of elements in Rock number " + (count + 1) + " are " + elements[count]);
        int noOfGems = findGems(numberOfRocks, elements);
        System.out.println(noOfGems);
    }

    private static int findGems(int numberOfRocks, String[] elements) {
        HashMap<Character, Integer> gemElements = new LinkedHashMap<Character, Integer>();
        populateElementsType(gemElements);
        for (int i = 1; i <= numberOfRocks; i++) {
            if (printInfo) {
                System.out.println("Unique Elements found till now " + gemElements.toString());
                System.out.println("Calculating gem stones in rock number " + i);
            }
            String elementsInRock = elements[i - 1];
            char[] chars = elementsInRock.toCharArray();
            boolean foundSomeElement = false;
            for (int keys = 0; keys < chars.length; keys++) {
                int prevWeight = calculateWeight(i - 1);
                int currentWeight = calculateWeight(i);
                if (i == 1)
                    gemElements.put(chars[keys], 1);
                else if (gemElements.get(chars[keys]) == prevWeight)
                    gemElements.put(chars[keys], currentWeight);

            }
            if (printInfo)
                System.out.println("Elements found in rock number " + i + " is " + gemElements.toString());
        }
        int result = 0;
        int ans = calculateWeight(numberOfRocks);
        if (printInfo)
            System.out.println("Elements with weight " + ans + " are Gem Elements");
        for (Integer values : gemElements.values())
            if (values == ans)
                result++;
        return result;
    }

    private static Integer calculateWeight(Integer n) {
        return (n * (n + 1)) / 2;
    }

    private static void populateElementsType(HashMap<Character, Integer> gemElements) {
        for (int elementCount = 0; elementCount < elementsType.length; elementCount++) {
            gemElements.put(elementsType[elementCount], 0);
        }
    }

    private static void resetGemCount(HashMap<Character, Integer> gemElements) {
        for (Character keys : gemElements.keySet()) {
            gemElements.put(keys, gemElements.get(keys) - 1);
        }
    }
}