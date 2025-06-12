##---white box test & cyclomatic complexcity---
import inspect


def sample_function(x):
    if x > 0:
        print("Positive number")
    elif x < 0:
        print("Negative number")
    else:
        print("Zero")

def sample_function_modified(x):
    if x > 0:
        for i in range(x):
            if i%2==0:
                print(i,":is EVEN")
            else :
                print(i,": is ODD")
    elif x > 0:
        print("NEGATIVE number")
    else :
        print("Number is ZERO")

def calculate_cyclomatic_complexity(function_code):
    """
    cc[cyclomatic complexity] = E - N +2P
    E[edges] = Decision points +1
    N[nodes] = statments
    p[P]     = connected components

    """
    decision_keywords= ['if','elif','where','for','case','except']
    lines = function_code.split('\n')
    decision = 0
    nodes = 0

    for line in lines:
        line = line.strip()
        if line == '' or line.startswith('#'):
            continue  
        nodes += 1
        for keyword in decision_keywords:
            if line.startswith(keyword):
                decision += 1
    edges = decision +1
    complexicity = edges - nodes + 2 
    return complexicity

def display_control_flow():
    print("control flow of the program:")
    print("  [Start]")
    print("     |")
    print("  [Check x > 0]")
    print("      /     \\")
    print("  Yes/       \\ No")
    print("[Print Positive] [Check x < 0]")
    print("                     /     \\")
    print("                Yes /       \\ No")
    print("        [Print Negative] [Print Zero]")
    print("                   \\     /")
    print("                    [End]")


def control_flow_demo(x):
   def control_flow_demo(x):
    print("\nControl Flow Execution for input:", x)
    print("Start")
    if x > 0:
        print("Decision: x > 0 → True path")
    elif x < 0:
        print("Decision: x < 0 → True path")
    else:
        print("Else path (Zero)")
    print("End")

print("---- Analyzing Original 'sample_function' ----")
function_source = inspect.getsource(sample_function)
complexity = calculate_cyclomatic_complexity(function_source)
print("Cyclomatic Complexity of 'sample_function' is:", complexity)
control_flow_demo(10)

display_control_flow()

# Analyze modified function
print("\n---- Analyzing Modified 'sample_function_modified' ----")
function_source_modified = inspect.getsource(sample_function_modified)
complexity_modified = calculate_cyclomatic_complexity(function_source_modified)
print("Cyclomatic Complexity of 'sample_function_modified' is:", complexity_modified)
