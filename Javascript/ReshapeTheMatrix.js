/**
 * @param {number[][]} nums
 * @param {number} r
 * @param {number} c
 * @return {number[][]}
 */
var matrixReshape = function (nums, r, c) {
  if (r * c !== nums.length * nums[0].length) {
    return nums;
  }

  var newArray = new Array (r);
  for (var i = 0; i < r; i++) {
    newArray[i] = new Array (c);
  }

  var counter = 0;
  for (var row = 0; row < nums.length; row++) {
    // newArray.push(0);
    for (var col = 0; col < nums[0].length; col++) {
      // console.log(counter / c);
      // console.log(counter % c);
      // console.log(nums[row][col]);

      newArray[Math.trunc(counter / c)][counter % c] = (nums[row][col]);
      counter++;
    }
  }
  return newArray;
};

console.log(matrixReshape([[1, 2], [3, 4]], 1, 4));
