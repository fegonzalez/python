
def test_call_by_object_reference (param):
    """Testing call by object-reference over mutable objects (e.g. list). 
       Checked: param changed after call"""
    print("type(param): ", type(param))
    # print("param (inside f)::1 : ", param)
    param[-1]=("added_inside__function")
    param[0]=222.333
    # print("param (inside f)::2 : ", param)



### just to test script. Remove otherwise.
if __name__ == '__main__':
    mutable_param= ["a1", "b2", 33];
    print("param (off-before call f) : ", mutable_param)
    test_call_by_object_reference(mutable_param)
    print("param (off-after  call f) : ", mutable_param)
        
