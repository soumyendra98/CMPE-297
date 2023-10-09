//write test code here to see user has given input or not
//if user has given input then call the function
//else show error message
//test case 1
describe("getSongs", function() {
    it("should return true if user has given input", function() {
        expect(getSongs("pop")).toBe(true);
    });
});
