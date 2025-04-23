/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let count = init; 
    
    return {
        increment: function() {
            return ++count;  
        },
        decrement: function() {
            return --count;  
        },
        reset: function() {
            count = init; 
            return count;
        }
    };
};
