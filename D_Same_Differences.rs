use std::io::{BufRead, BufReader, Result, stdin};

fn main() -> Result<()> {
    let input = stdin();
    let mut reader = BufReader::new(input);
    let mut buf = String::new();
    reader.read_line(&mut buf)?;

    for _ in 0..buf.trim().parse::<i32>().unwrap() {
        buf.clear();
        reader.read_line(&mut buf)?;
        let _ = buf.trim().parse::<i32>().unwrap();
        buf.clear();
        reader.read_line(&mut buf)?;
        let nums = buf.split_whitespace().map(|v| v.parse::<i32>().unwrap()).collect::<Vec<_>>();
        
        let result = solve(nums);

        println!("{result}");
    }

    Ok(())
}

fn solve(nums: Vec<i32>) -> i64 {
    let mut res = 0;

    let mut dict = std::collections::HashMap::new();

    for i in 0..nums.len() {
        let diff = nums[i] - i as i32;
        let count = dict.entry(diff).or_insert(0i64);
        res += *count;
        *count += 1;
    }

    res
}