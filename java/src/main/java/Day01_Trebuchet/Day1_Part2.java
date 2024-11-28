package Day01_Trebuchet;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Day1_Part2 {
    List<String> NUMBERS = List.of("one", "two", "three", "four", "five", "six", "seven", "eight", "nine");

    public static void main(String[] args) {
        Day1_Part2 day1 = new Day1_Part2();
        String filePath = "C:\\Users\\shiva\\Documents\\GitHub Repos\\Advent-Of-Code-2023\\java\\src\\main\\java\\Day01_Trebuchet\\input.txt";

        List<Integer> calibrationValues = day1.parseFile(filePath);
        // System.out.println(calibrationValues.size());
        int sum = 0;

        for (int value : calibrationValues) sum += value;

       System.out.println("Sum of numbers: " + sum);
    }

    public List<Integer> parseFile(String filePath) {
        List<Integer> numbers = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))){
            String line;

            while ((line = br.readLine()) != null) {
                int parsedNumber = parseLine(line);
                if (parsedNumber != -1) numbers.add(parsedNumber);
            }
        } catch (IOException e) {
            System.out.println("File not found");
        }

        return numbers;
    }

    private int parseLine(String line) {
        List<String> results = new ArrayList<>();
        int index = 0;

        while (index < line.length()) {
            char currentChar = line.charAt(index);

            if (Character.isDigit(currentChar)) {
                results.add(String.valueOf(currentChar));
                index++;
                continue;
            }

            for (String word : NUMBERS) {
                if (line.substring(index).startsWith(word)) {
                    results.add(String.valueOf(
                            NUMBERS.indexOf(word) + 1
                    ));

                    index += word.length() - 2;
                    break;
                }
            }

            index++;
        }

        if (!results.isEmpty()) return Integer.parseInt(results.getFirst() + results.getLast());

        return -1; // If no valid number is found
    }
}
