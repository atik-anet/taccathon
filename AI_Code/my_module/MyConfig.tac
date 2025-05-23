// Copyright (c) 2024 Arista Networks, Inc.  All rights reserved.
// Arista Networks, Inc. Confidential and Proprietary.

// Define a namespace for the module
MyModule : Tac::Namespace {

// Define a configuration type with a counter
MyConfigType : Tac::Type() : Tac::PtrInterface {
   `hasFactoryFunction;
   `isNotifyingByDefault;

   // A simple counter value
   counter : U32;

   // Method to increment the counter
   incrementCounter : extern invasive void();
}

// Define a status type to report the counter value
MyStatusType : Tac::Type() : Tac::PtrInterface {
   `hasFactoryFunction;
   `isNotifyingByDefault;

   // The current counter value from the config
   currentCounterValue : U32;
}

// Define a Constrainer to react to config changes
MyConstrainer : Tac::Type( myConfig, myStatus ) : Tac::Constrainer {
   `hasFactoryFunction;

   // Input: The configuration type
   myConfig : in MyModule::MyConfigType::PtrConst;
   // Output: The status type to update
   myStatus : MyModule::MyStatusType::Ptr;

   // External method to handle counter updates
   handleCounterUpdate : extern invasive void();

   // Event handler: Trigger when the counter in myConfig changes
   when myConfig::counter => handleCounterUpdate();

   // Initial handler: Set initial status on startup
   handleInitialized : extern invasive void();
   this => initially handleInitialized();
}


} // namespace MyModule

// Include the corresponding C++ implementation file
<<= CppBlock("MyConfig.tin");