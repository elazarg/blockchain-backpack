#!/usr/bin/python
#
# Depends on https://github.com/ethermarket/ethertdd.

import unittest
from ethereum import tester
from ethertdd import FileContractStore

# Up the gas limit because our contract is pretty huge.
tester.gas_limit = 10000000;

kOK = 'OK\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
kPermissionDenied = 'Permission Denied\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
kNullString = '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

fs = FileContractStore()

class UsersAndPermissionsTest(unittest.TestCase):
    def setUp(self):
        self.t = tester.state()
        self.t.mine()
        self.contract = fs.BackpackSystem.create(sender=tester.k0,
                                                 state=self.t)
        self.t.mine()

    def test_creator_has_all_permissions(self):
        for i in [0, 1, 2, 3, 4, 5]:
            self.assertTrue(self.contract.HasPermission(tester.a0, i))
        for i in [6, 7, 142]:
            self.assertFalse(self.contract.HasPermission(tester.a0, i))

    def test_other_contact_has_no_permissions_by_default(self):
        for i in [0, 1, 2, 3, 4, 5, 6, 7, 142]:
            self.assertFalse(self.contract.HasPermission(tester.a1, i))

    def test_other_contract_gets_a_permission(self):
        # Starts without the permission.
        self.assertFalse(self.contract.HasPermission(tester.a1, 4));

        # Can't take a permission by itself (AddAtributesToItem).
        self.assertEquals(
            self.contract.SetPermission(tester.a1, 4, True, sender=tester.k1),
            kPermissionDenied)
        self.t.mine()
        self.assertFalse(self.contract.HasPermission(tester.a1, 4))

        # Gets the permission from the contract creater.
        self.assertEquals(
            self.contract.SetPermission(tester.a1, 4, True, sender=tester.k0),
            kOK)
        self.t.mine()
        self.assertTrue(self.contract.HasPermission(tester.a1, 4))

    def test_allow_items(self):
        # Create a user
        self.assertEquals(self.contract.CreateUser(tester.a1), kOK);
        self.assertTrue(self.contract.AllowsItemsReceived(tester.a1));

        # The user can turn off the ability to receive items.
        self.contract.SetAllowItemsReceived(False, sender=tester.k1);
        self.assertFalse(self.contract.AllowsItemsReceived(tester.a1));

    def test_user_cant_create_self(self):
        self.assertEquals(self.contract.CreateUser(tester.a1, sender=tester.k1),
                          kPermissionDenied);
        self.assertEquals(self.contract.GetBackpackCapacityFor(tester.a1), 0);

    def test_user_cant_grant_self_capacity(self):
        # Build the user.
        self.assertEquals(self.contract.CreateUser(tester.a1), kOK);
        self.assertEquals(self.contract.GetBackpackCapacityFor(tester.a1), 300);

        # Ensure the user can't grant self more backpack space.
        self.assertEquals(self.contract.AddBackpackCapacityFor(
            tester.a1, sender=tester.k1), kPermissionDenied);
        self.assertEquals(self.contract.GetBackpackCapacityFor(tester.a1), 300);

    def test_can_grant_capacity(self):
        # Build the user.
        self.assertEquals(self.contract.CreateUser(tester.a1), kOK);
        self.assertEquals(self.contract.GetBackpackCapacityFor(tester.a1), 300);

        self.assertEquals(self.contract.AddBackpackCapacityFor(tester.a1), kOK);
        self.assertEquals(self.contract.GetBackpackCapacityFor(tester.a1), 400);

class AttributeTest(unittest.TestCase):
    def setUp(self):
        self.t = tester.state()
        self.t.mine()
        self.contract = fs.BackpackSystem.create(sender=tester.k0,
                                                 state=self.t)
        self.t.mine()

    def test_modify_schema_permission(self):
        self.assertEquals(self.contract.SetAttribute(1, "Two", "Three", sender=tester.k1),
                          kPermissionDenied);

    def test_cant_set_zero(self):
        self.assertEquals(self.contract.SetAttribute(0, "Zero", "Emptiness is Loneliness"),
                          'Invalid Attribute\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00');
        self.assertEquals(self.contract.GetAttribute(0, "Zero"), kNullString);

    def test_can_set_property(self):
        self.assertEquals(self.contract.SetAttribute(1, "One", "1"), kOK);
        self.assertEquals(self.contract.GetAttribute(1, "One"),
                          '1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00');

class SchemaTest(unittest.TestCase):
    def setUp(self):
        self.t = tester.state()
        self.t.mine()
        self.contract = fs.BackpackSystem.create(sender=tester.k0,
                                                 state=self.t)
        self.t.mine()

    def test_schema_permission(self):
        self.assertEquals(self.contract.SetItemSchema(18, 5, 25, 0, sender=tester.k1),
                          kPermissionDenied);

    def test_schema_set_and_get_level(self):
        self.assertEquals(self.contract.SetItemSchema(18, 5, 25, 0), kOK);
        self.assertEquals(self.contract.GetItemLevelRange(18), [5, 25]);

if __name__ == '__main__':
    unittest.main()