
def before_all(context):
     print("Executing before all")
     print("======================================================\n")

def before_feature(context, feature):
     print("Before feature\n")
     print("======================================================\n")

def before_scenario(context,scenario):
    print("Before scenario\n")
    print("======================================================\n")

def after_scenario(context,scenario):
    # context.browser.quit()
    print("After scenario\n")
    print("======================================================\n")

def after_feature(context,feature):
     print("After feature\n")
     print("======================================================\n")

def after_all(context):
     print("Executing after all")
     print("======================================================\n")
