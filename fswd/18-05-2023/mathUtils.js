class MathUtils {
  static sum(arr) {
    return arr.reduce((sum, num) => sum + num, 0);
  }

  static average(arr) {
    return MathUtils.sum(arr)/length;
  }

  static max(arr) {
    let maximum = arr[0];
    arr.forEach(element => {
      if(element > maximum) {
        maximum = element;
      }
    });
    return maximum;
  }

  static min(arr) {
    let minimum = arr[0];
    arr.forEach(element => {
      if(element < minimum) {
        minimum = element;
      }
    });
    return minimum;
  }
} 
const arr = [1, 2, 2, 4];
console.log('Sum:', MathUtils.sum(arr));
console.log('Average:', MathUtils.average(arr));
console.log('Max:', MathUtils.max(arr));
console.log('Min:', MathUtils.min(arr));
