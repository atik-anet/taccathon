// Copyright (c) 2024 Arista Networks, Inc.  All rights reserved.
// Arista Networks, Inc. Confidential and Proprietary.

MyCounter : Tac::Type() : Tac::PtrInterface {
   `isNotifyingByDefault;
   // A simple counter attribute
   counter : U32 = initially 0;

   // Method to increment the counter
   increment : extern invasive void();
}

MyCounterStatus : Tac::Type() : Tac::PtrInterface {
   `isNotifyingByDefault;
   currentCount : U32 = initially 0;
}

MyCounterReactor : Tac::Type( counterConfig ) : Tac::Constrainer {
   `hasFactoryFunction;

   counterConfig : in MyCounter::PtrConst;
   counterStatus : MyCounterStatus::Ptr;

   // Reactor method to handle counter changes
   handleCounterChange : extern invasive void();

   // React to changes in the counterConfig's counter attribute
   counterConfig::counter => handleCounterChange();

   // Initialize the status when the constrainer is created
   this => initially handleCounterChange();
}