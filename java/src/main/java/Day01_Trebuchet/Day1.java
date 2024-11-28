package Day01_Trebuchet;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Day1 {
    public static void main(String[] args) {
        String filePath = "input.txt";

        List<Integer> numbers = new ArrayList<>();
        int sum = 0;

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))){
            String line;

            while((line = br.readLine()) != null) {
                String[] digits = line.replaceAll("\\D", "").split("");
                if (digits.length > 0) {
                    int number = Integer.parseInt(digits[0] + digits[digits.length - 1]);
                    numbers.add(number);
                } else break;
            }
        } catch (IOException e) {
            System.out.println("File not found");
        }

        for (int number : numbers) sum += number;

        System.out.println("Sum of numbers: " + sum);
    }
}
